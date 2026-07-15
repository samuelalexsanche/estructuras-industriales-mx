/* =====================================================================
   ESTRUCTURAS INDUSTRIALES MX — Cloudflare Worker (proxy del asistente IA)
   ---------------------------------------------------------------------
   Guarda la API key de DeepSeek como SECRETO del Worker (nunca en el repo):
       npx wrangler secret put DEEPSEEK_API_KEY

   Despliegue:
       cd worker && npx wrangler deploy
   Copia la URL resultante y pégala en  js/chat.js → CHAT_ENDPOINT.

   Qué hace: recibe {messages:[{role,content}]}, antepone el "system prompt"
   con la información de la empresa (editable abajo) y transmite en streaming
   la respuesta del modelo real (DeepSeek) de vuelta al navegador.
   ===================================================================== */

// Orígenes autorizados a llamar al Worker (evita que otros gasten tu key).
// Agrega/ajusta tu dominio real de GitHub Pages o dominio propio.
const ALLOWED_ORIGINS = [
  'https://samuelalexsanche.github.io',
  'http://localhost:8099',
  'http://localhost:8080',
  'http://127.0.0.1:8099',
];

// ====== INFORMACIÓN DE LA EMPRESA (edítala libremente) ======
const SYSTEM_PROMPT = `
Eres el asistente virtual de "Estructuras Industriales MX", una empresa mexicana de
construcción industrial y montaje de estructura de acero. Respondes preguntas de
visitantes del sitio web.

QUÉ HACE LA EMPRESA:
- Diseño, fabricación y montaje de estructura metálica y obra industrial "llave en mano".
- Ingeniería de detalle y modelado 3D / BIM.
- Fabricación en taller con control de calidad por lote.
- Montaje certificado en obra bajo estándares internacionales de seguridad y calidad.
- "De la cimentación al último tornillo."

SECTORES QUE ATIENDE:
- Automotriz: naves de producción, líneas de ensamble, plantas de autopartes.
- Farmacéutica: cuartos limpios, plantas GMP, control de contaminación.
- Logístico: centros de distribución y almacenes de gran claro para operación 24/7.
- Alimenticio: plantas de proceso y frío con acabados sanitarios e inocuidad.
- Aeronáutico: hangares y naves de gran claro libre de columnas.

CIFRAS DE RESPALDO (aproximadas, de referencia):
- +850,000 m² construidos · +42,000 toneladas de estructura montada.
- +240 proyectos entregados · 99% de entregas en tiempo · 18 años de experiencia.

COBERTURA Y CONTACTO:
- Base en Guadalajara, Jalisco, México (operan a nivel nacional).
- Teléfono/WhatsApp: +52 33 2787 4747
- Correo: contacto@estructurasindustriales.mx
- Ofrecen visita técnica y anteproyecto sin costo, y contacto de un ingeniero en <24 h.

CÓMO RESPONDER:
- Responde SIEMPRE en el idioma del usuario (por defecto español), con tono profesional,
  claro y cercano. Sé breve (2-5 frases) salvo que pidan detalle.
- Habla solo de la empresa y de construcción/estructura industrial. Si preguntan algo
  fuera de tema, redirige amablemente a lo que sí puedes ayudar.
- NO inventes precios, plazos exactos ni datos que no tengas. Para cotizaciones o números
  concretos, invita a dejar sus datos en el formulario o a escribir por WhatsApp.
- Si no sabes algo, dilo con honestidad y ofrece contactar a un ingeniero.
- Este es un sitio de demostración con datos de ejemplo; si preguntan por casos o clientes
  específicos, acláralo sin inventar.
`.trim();

function corsHeaders(origin) {
  const allow = ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0];
  return {
    'Access-Control-Allow-Origin': allow,
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400',
    'Vary': 'Origin',
  };
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get('Origin') || '';
    const cors = corsHeaders(origin);

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: cors });
    }
    if (request.method !== 'POST') {
      return json({ error: 'Method not allowed' }, 405, cors);
    }
    if (!env.DEEPSEEK_API_KEY) {
      return json({ error: 'Falta configurar DEEPSEEK_API_KEY como secreto del Worker.' }, 500, cors);
    }

    let payload;
    try {
      payload = await request.json();
    } catch {
      return json({ error: 'JSON inválido.' }, 400, cors);
    }

    // Sanea el historial recibido del navegador.
    let messages = Array.isArray(payload.messages) ? payload.messages : [];
    messages = messages
      .filter((m) => m && (m.role === 'user' || m.role === 'assistant') && typeof m.content === 'string')
      .slice(-12)
      .map((m) => ({ role: m.role, content: m.content.slice(0, 4000) }));

    if (!messages.length) {
      return json({ error: 'Sin mensajes.' }, 400, cors);
    }

    const finalMessages = [{ role: 'system', content: SYSTEM_PROMPT }, ...messages];

    let upstream;
    try {
      upstream = await fetch('https://api.deepseek.com/chat/completions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${env.DEEPSEEK_API_KEY}`,
        },
        body: JSON.stringify({
          model: 'deepseek-chat',
          messages: finalMessages,
          stream: true,
          temperature: 0.3,
          max_tokens: 700,
        }),
      });
    } catch (err) {
      return json({ error: 'No se pudo contactar al modelo.' }, 502, cors);
    }

    if (!upstream.ok || !upstream.body) {
      const detail = await upstream.text().catch(() => '');
      return json({ error: 'Error del modelo', status: upstream.status, detail }, 502, cors);
    }

    // Transmite el SSE de DeepSeek tal cual al navegador.
    return new Response(upstream.body, {
      status: 200,
      headers: {
        ...cors,
        'Content-Type': 'text/event-stream; charset=utf-8',
        'Cache-Control': 'no-cache',
        Connection: 'keep-alive',
      },
    });
  },
};

function json(obj, status, cors) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { ...cors, 'Content-Type': 'application/json' },
  });
}
