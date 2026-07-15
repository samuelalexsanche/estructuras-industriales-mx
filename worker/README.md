# Asistente IA — Cloudflare Worker (proxy DeepSeek)

Este Worker hace de intermediario seguro entre la página estática y el modelo real
(**DeepSeek**). La API key vive aquí como **secreto cifrado**, nunca en el sitio público.

```
Navegador (js/chat.js)  →  Cloudflare Worker (esta carpeta)  →  DeepSeek API
                            (guarda DEEPSEEK_API_KEY)            (modelo real)
```

## Requisitos
- Cuenta gratis en https://dash.cloudflare.com
- Node.js instalado (para `npx wrangler`)
- Una API key de DeepSeek: https://platform.deepseek.com → API Keys

## Despliegue (una sola vez)

```bash
cd worker

# 1) Inicia sesión en Cloudflare (abre el navegador)
npx wrangler login

# 2) Guarda tu API key de DeepSeek como secreto (te la pedirá al ejecutar)
npx wrangler secret put DEEPSEEK_API_KEY

# 3) Publica el Worker
npx wrangler deploy
```

Al terminar, `wrangler` imprime una URL tipo:

```
https://estructuras-chat.TU-SUBDOMINIO.workers.dev
```

## Conectar la página

1. Copia esa URL.
2. Ábrela en `../js/chat.js` y pégala en la constante:
   ```js
   const CHAT_ENDPOINT = 'https://estructuras-chat.TU-SUBDOMINIO.workers.dev';
   ```
3. Commit + push. Listo: el chat ya responde con el modelo real.

## Personalizar
- **Info de la empresa** que usa el asistente → variable `SYSTEM_PROMPT` en `worker.js`.
- **Orígenes permitidos** (qué dominios pueden usar tu key) → `ALLOWED_ORIGINS` en `worker.js`.
  Incluye tu dominio real de GitHub Pages / dominio propio antes de producción.
- **Modelo / creatividad** → `model`, `temperature`, `max_tokens` en `worker.js`.

## Costo
DeepSeek es muy económico y Cloudflare Workers tiene una capa gratuita amplia
(100k solicitudes/día). Para un demo o tráfico bajo, el costo es prácticamente nulo.
