/* =====================================================================
   ESTRUCTURAS INDUSTRIALES MX — Asistente IA (chat)
   Modelo real (DeepSeek) vía Cloudflare Worker. La API key vive en el
   Worker (secreto), nunca en este archivo público. Respuestas en streaming.
   ---------------------------------------------------------------------
   ⚙️  CONFIGURA AQUÍ: pega la URL de tu Worker ya desplegado con wrangler.
       Ej: 'https://estructuras-chat.tu-sub.workers.dev'
   Mientras esté vacío, el chat avisa que falta conectarlo (no inventa nada).
   ===================================================================== */
(function () {
  'use strict';

  const CHAT_ENDPOINT = ''; // ←←← PEGA AQUÍ LA URL DE TU CLOUDFLARE WORKER

  const fab   = document.getElementById('aiFab');
  const panel = document.getElementById('aiPanel');
  const close = document.getElementById('aiClose');
  const body  = document.getElementById('aiBody');
  const form  = document.getElementById('aiForm');
  const input = document.getElementById('aiInput');
  const send  = document.getElementById('aiSend');
  const chips = document.getElementById('aiChips');
  if (!fab || !panel) return;

  /* Historial de la conversación (lo que se manda al modelo).
     El "system prompt" con la info de la empresa vive en el Worker. */
  const history = [];
  let busy = false;
  let greeted = false;

  const WELCOME =
    '¡Hola! 👷 Soy el asistente de Estructuras Industriales MX. ' +
    'Puedo resolver dudas sobre lo que hacemos: sectores, fabricación y montaje ' +
    'de estructura de acero, zonas donde operamos y cómo cotizar. ¿En qué te ayudo?';

  /* ---------- Abrir / cerrar ---------- */
  function openPanel() {
    panel.hidden = false;
    // permite que el navegador aplique 'hidden=false' antes de animar
    requestAnimationFrame(() => panel.classList.add('open'));
    fab.classList.add('hidden');
    if (!greeted) { addMessage('bot', WELCOME); greeted = true; }
    setTimeout(() => input.focus(), 250);
  }
  function closePanel() {
    panel.classList.remove('open');
    fab.classList.remove('hidden');
    setTimeout(() => { panel.hidden = true; }, 320);
  }
  fab.addEventListener('click', openPanel);
  close.addEventListener('click', closePanel);
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && panel.classList.contains('open')) closePanel();
  });

  /* ---------- Auto-resize del textarea + Enter para enviar ---------- */
  input.addEventListener('input', () => {
    input.style.height = 'auto';
    input.style.height = Math.min(input.scrollHeight, 110) + 'px';
  });
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); form.requestSubmit(); }
  });

  /* ---------- Chips de sugerencias ---------- */
  chips.addEventListener('click', (e) => {
    const btn = e.target.closest('.ai-chip');
    if (!btn || busy) return;
    input.value = btn.textContent;
    form.requestSubmit();
  });

  /* ---------- Render de mensajes ---------- */
  function addMessage(role, text) {
    const wrap = document.createElement('div');
    wrap.className = 'ai-msg ai-msg--' + (role === 'user' ? 'user' : 'bot');
    const bubble = document.createElement('div');
    bubble.className = 'ai-msg__bubble';
    bubble.textContent = text;
    wrap.appendChild(bubble);
    body.appendChild(wrap);
    scrollDown();
    return bubble;
  }
  function addTyping() {
    const wrap = document.createElement('div');
    wrap.className = 'ai-msg ai-msg--bot';
    wrap.innerHTML =
      '<div class="ai-msg__bubble"><span class="ai-typing"><i></i><i></i><i></i></span></div>';
    body.appendChild(wrap);
    scrollDown();
    return wrap;
  }
  function scrollDown() { body.scrollTop = body.scrollHeight; }

  /* ---------- Envío ---------- */
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const text = input.value.trim();
    if (!text || busy) return;

    chips.style.display = 'none';
    addMessage('user', text);
    history.push({ role: 'user', content: text });
    input.value = '';
    input.style.height = 'auto';
    setBusy(true);

    // Sin endpoint configurado: aviso honesto (no una respuesta inventada).
    if (!CHAT_ENDPOINT) {
      const typing = addTyping();
      setTimeout(() => {
        typing.remove();
        addMessage(
          'bot',
          '⚙️ El asistente aún no está conectado a un modelo. Falta pegar la URL ' +
          'del Cloudflare Worker en js/chat.js (CHAT_ENDPOINT). Una vez conectado, ' +
          'responderé con un modelo real en tiempo real.'
        );
        setBusy(false);
      }, 700);
      return;
    }

    const typing = addTyping();
    let bubble = null;
    let acc = '';

    try {
      const res = await fetch(CHAT_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ messages: history.slice(-12) }),
      });
      if (!res.ok || !res.body) throw new Error('HTTP ' + res.status);

      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let buffer = '';

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });

        // SSE: líneas "data: {json}" separadas por doble salto de línea
        const parts = buffer.split('\n');
        buffer = parts.pop() || '';
        for (const line of parts) {
          const trimmed = line.trim();
          if (!trimmed.startsWith('data:')) continue;
          const payload = trimmed.slice(5).trim();
          if (payload === '[DONE]') continue;
          try {
            const json = JSON.parse(payload);
            const delta = json.choices?.[0]?.delta?.content || '';
            if (delta) {
              acc += delta;
              if (!bubble) { typing.remove(); bubble = addMessage('bot', ''); }
              bubble.textContent = acc;
              scrollDown();
            }
          } catch (_) { /* fragmento parcial, se completa en la próxima vuelta */ }
        }
      }

      if (!acc) { typing.remove(); acc = 'No obtuve respuesta. Intenta de nuevo.'; addMessage('bot', acc); }
      history.push({ role: 'assistant', content: acc });
    } catch (err) {
      typing.remove();
      addMessage(
        'bot',
        'Ups, hubo un problema al conectar con el asistente. Revisa tu conexión o ' +
        'inténtalo de nuevo en un momento. Mientras tanto puedes escribirnos por WhatsApp.'
      );
      console.error('[chat] error:', err);
    } finally {
      setBusy(false);
    }
  });

  function setBusy(v) {
    busy = v;
    send.disabled = v;
    input.disabled = v;
    if (!v) input.focus();
  }
})();
