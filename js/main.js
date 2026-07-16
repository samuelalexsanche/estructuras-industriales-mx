/* =====================================================================
   ESTRUCTURAS INDUSTRIALES MX — Interacciones
   Vanilla JS, sin dependencias. Compatible con GitHub Pages.
   ===================================================================== */
(function () {
  'use strict';
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Año dinámico en footer ---------- */
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---------- Nav: sólido al hacer scroll ---------- */
  const nav = document.getElementById('nav');
  const onScrollNav = () => nav.classList.toggle('scrolled', window.scrollY > 20);
  onScrollNav();
  window.addEventListener('scroll', onScrollNav, { passive: true });

  /* ---------- Menú móvil ---------- */
  const toggle = document.getElementById('navToggle');
  const links = document.getElementById('navLinks');
  if (toggle && links) {
    toggle.addEventListener('click', () => {
      const open = links.classList.toggle('open');
      toggle.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', String(open));
    });
    links.querySelectorAll('a').forEach((a) =>
      a.addEventListener('click', () => {
        links.classList.remove('open');
        toggle.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      })
    );
  }

  /* ---------- Reveal on scroll (IntersectionObserver) ---------- */
  const revealEls = document.querySelectorAll('.reveal');
  const statEls = document.querySelectorAll('.stat');
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add('in');
          io.unobserve(e.target);
        }
      });
    },
    { threshold: 0.15, rootMargin: '0px 0px -8% 0px' }
  );
  revealEls.forEach((el) => io.observe(el));
  statEls.forEach((el) => io.observe(el));

  /* ---------- Contadores animados ---------- */
  const fmt = (n) => n.toLocaleString('es-MX');
  function animateCount(el) {
    const target = parseFloat(el.dataset.count || '0');
    const suffix = el.dataset.suffix || '';
    if (prefersReduced) { el.textContent = fmt(target) + suffix; return; }
    const dur = 1800;
    const start = performance.now();
    function tick(now) {
      const p = Math.min((now - start) / dur, 1);
      const eased = 1 - Math.pow(1 - p, 3); // easeOutCubic
      el.textContent = fmt(Math.floor(eased * target)) + suffix;
      if (p < 1) requestAnimationFrame(tick);
      else el.textContent = fmt(target) + suffix;
    }
    requestAnimationFrame(tick);
  }
  const countObs = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) { animateCount(e.target); countObs.unobserve(e.target); }
      });
    },
    { threshold: 0.4 }
  );
  document.querySelectorAll('[data-count]').forEach((el) => countObs.observe(el));

  /* ---------- Parallax en el hero ---------- */
  const parEls = document.querySelectorAll('[data-parallax]');
  if (!prefersReduced && parEls.length) {
    let ticking = false;
    const onScroll = () => {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(() => {
        const y = window.scrollY;
        parEls.forEach((el) => {
          const speed = parseFloat(el.dataset.parallax) || 0.2;
          el.style.transform = 'translate3d(0,' + y * speed + 'px,0)';
        });
        ticking = false;
      });
    };
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------- Partículas del hero ---------- */
  const particles = document.getElementById('particles');
  if (particles && !prefersReduced) {
    const N = 22;
    for (let i = 0; i < N; i++) {
      const p = document.createElement('i');
      p.style.left = Math.random() * 100 + '%';
      p.style.top = 60 + Math.random() * 40 + '%';
      const d = 6 + Math.random() * 8;
      p.style.animationDuration = d + 's';
      p.style.animationDelay = -Math.random() * d + 's';
      p.style.opacity = 0.2 + Math.random() * 0.4;
      particles.appendChild(p);
    }
  }

  /* ---------- Glow que sigue al cursor en tarjetas de sector ---------- */
  document.querySelectorAll('.sector').forEach((card) => {
    card.addEventListener('pointermove', (e) => {
      const r = card.getBoundingClientRect();
      card.style.setProperty('--mx', ((e.clientX - r.left) / r.width) * 100 + '%');
      card.style.setProperty('--my', ((e.clientY - r.top) / r.height) * 100 + '%');
    });
  });

  /* ---------- Reproductor de video (placeholder) ----------
     Cuando tengas el video real:
     1) Coloca el archivo en assets/video-empresa.mp4  (o usa un embed de YouTube/Vimeo)
     2) Reemplaza el bloque .player__poster por el <video> comentado en index.html
     Este handler solo avisa mientras no exista el video real.
  ------------------------------------------------------------------- */
  const playBtn = document.getElementById('playBtn');
  if (playBtn) {
    playBtn.addEventListener('click', () => {
      alert('Aquí se reproducirá el video corporativo. Reemplaza el placeholder por el video real en assets/ (ver comentarios en index.html).');
    });
  }

  /* ---------- Validación del formulario de leads ---------- */
  const form = document.getElementById('leadForm');
  const note = document.getElementById('formNote');
  if (form) {
    /* ---- Tipo de contacto: cliente / proveedor / empleo ---- */
    const intentInputs = form.querySelectorAll('input[name="intent"]');
    const groups = form.querySelectorAll('.intent-group');
    const lblMensaje = document.getElementById('lblMensaje');
    const lblEmpresa = document.getElementById('lblEmpresa');
    const submitBtn = document.getElementById('formSubmit');
    const intentCopy = {
      cliente:   { msg: 'Cuéntanos del proyecto',            empresa: 'Empresa',                  btn: 'Solicitar cotización' },
      proveedor: { msg: 'Qué ofreces: capacidad y experiencia', empresa: 'Empresa',               btn: 'Enviar propuesta' },
      empleo:    { msg: 'Cuéntanos de ti y tu experiencia',   empresa: 'Empresa actual (opcional)', btn: 'Enviar solicitud' },
    };
    const applyIntent = (val) => {
      groups.forEach((g) => { g.hidden = g.dataset.intent !== val; });
      const c = intentCopy[val] || intentCopy.cliente;
      if (lblMensaje) lblMensaje.textContent = c.msg;
      if (lblEmpresa) lblEmpresa.textContent = c.empresa;
      if (submitBtn) submitBtn.textContent = c.btn;
    };
    intentInputs.forEach((r) => r.addEventListener('change', () => applyIntent(r.value)));
    const checked = form.querySelector('input[name="intent"]:checked');
    applyIntent(checked ? checked.value : 'cliente');

    const setError = (input, msg) => {
      const field = input.closest('.field') || input.parentElement.closest('.field');
      const small = input.parentElement.querySelector('.err') || (field && field.querySelector('.err'));
      if (field) field.classList.toggle('invalid', !!msg);
      if (small) small.textContent = msg || '';
    };
    const validators = {
      nombre: (v) => (v.trim().length >= 2 ? '' : 'Escribe tu nombre.'),
      telefono: (v) => (/[0-9]{7,}/.test(v.replace(/\D/g, '')) ? '' : 'Teléfono no válido.'),
      email: (v) => (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) ? '' : 'Correo no válido.'),
    };

    form.querySelectorAll('input,select').forEach((input) => {
      input.addEventListener('blur', () => {
        if (validators[input.name]) setError(input, validators[input.name](input.value));
      });
    });

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      let ok = true;
      Object.keys(validators).forEach((name) => {
        const input = form.elements[name];
        if (!input) return;
        const msg = validators[name](input.value);
        setError(input, msg);
        if (msg) ok = false;
      });

      if (!ok) {
        note.textContent = 'Revisa los campos marcados.';
        note.className = 'form-note bad';
        return;
      }

      /* DEMO: no hay backend. Aquí conectarías tu endpoint / servicio de correo.
         Ej: fetch('/api/lead', { method:'POST', body: new FormData(form) }) */
      note.textContent = '¡Gracias! Recibimos tu solicitud. Un ingeniero te contactará en menos de 24 h.';
      note.className = 'form-note ok';
      form.reset();
      setTimeout(() => { note.textContent = ''; note.className = 'form-note'; }, 6000);
    });
  }
})();
