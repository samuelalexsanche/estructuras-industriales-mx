# Estructuras Industriales MX — Landing page

Sitio web de una sola página para una empresa de **construcción industrial y montaje de estructura de acero**.
Diseño oscuro, técnico (estética render 3D / blueprint), con animaciones, parallax y efectos de scroll. Sin frameworks ni build: HTML, CSS y JS puros → despliega directo en **GitHub Pages**.

## Estructura

```
constructora-industrial/
├── index.html          # Página completa (todas las secciones)
├── css/styles.css      # Sistema de diseño + animaciones (tokens editables arriba)
├── js/main.js          # Reveals, contadores, parallax, validación de form
├── assets/
│   └── favicon.svg
└── README.md
```

## Secciones incluidas

1. **Hero** con fondo blueprint animado (wireframe de nave que se "dibuja") + parallax + partículas.
2. **Nosotros / Video de la empresa** (reproductor placeholder listo para el video real).
3. **Cifras** — contadores animados: m² construidos, toneladas de estructura montada, proyectos, % en tiempo.
4. **Sectores** — automotriz, farmacéutica, logístico, alimenticio, aeronáutico + acceso a proyectos.
5. **Últimos proyectos** — galería tipo mosaico.
6. **Clientes** — marquee infinito de logos.
7. **Formulario de contacto** para prospectos con validación en el navegador.
8. **Burbuja flotante de WhatsApp**.
9. **Asistente IA** — chat flotante que responde con un **modelo real** (DeepSeek) sobre la
   información de la empresa. La API key vive en un Cloudflare Worker, nunca en el sitio.
   Ver `worker/README.md` para desplegarlo y `js/chat.js` para conectar la URL.

## Cómo verlo localmente

Abre `index.html` en el navegador, o levanta un servidor:

```bash
python3 -m http.server 8080
# luego abre http://localhost:8080
```

## Qué personalizar (todo es placeholder editable)

| Qué | Dónde |
|-----|-------|
| Nombre / marca | Texto "Estructuras Industriales MX" en `index.html` |
| Colores | Variables `--primary`, `--accent`, etc. al inicio de `css/styles.css` (paleta actual: monocromo frío, sin naranja) |
| Info que usa el asistente IA | `SYSTEM_PROMPT` en `worker/worker.js` |
| Conectar el asistente IA | `CHAT_ENDPOINT` en `js/chat.js` (URL del Worker) |
| Cifras (m², toneladas…) | Atributos `data-count` en `index.html` |
| Video de la empresa | Reemplaza el `.player__poster` por el `<video>` comentado en `index.html` |
| Logos de clientes | Bloque `.marquee__track` en `index.html` |
| Proyectos | Bloque `.proyectos__grid` en `index.html` |
| Teléfono / WhatsApp | `href="tel:..."` y `href="https://wa.me/52..."` en `index.html` |
| Correo | `mailto:` en `index.html` |
| Envío del formulario | Función submit en `js/main.js` (conectar backend / servicio de correo) |

## Fondos con IA (opcional)

Los fondos actuales son 100% código (ligeros, sin dependencias). Si quieres reemplazarlos por
renders generados con IA (kie.ai u otro), coloca las imágenes en `assets/` y cámbialas en:
- Hero: `.hero__bg`
- Proyectos: `.proj__media[data-scene]` en `css/styles.css`

## Deploy en GitHub Pages

Ver el prompt de continuación entregado en el chat (incluye pasos de repo + Pages).
