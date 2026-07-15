# Desplegar en Vercel (con el asistente IA funcionando)

El sitio es estático y el asistente IA corre como **función serverless** en `api/chat.js`.
La API key de DeepSeek va como **variable de entorno** en Vercel (nunca en el repo).

## Pasos (todo con clics, ~2 min)

1. Entra a **https://vercel.com** e inicia sesión con tu cuenta de **GitHub**.
2. Clic en **Add New… → Project**.
3. En **Import Git Repository**, elige `samuelalexsanche/estructuras-industriales-mx`.
   - Si no aparece, clic en *Adjust GitHub App Permissions* y dale acceso al repo.
4. **Framework Preset:** deja **Other** (no hay build). No cambies nada más.
5. Abre **Environment Variables** y agrega:
   - **Name:** `DEEPSEEK_API_KEY`
   - **Value:** tu API key de DeepSeek (empieza con `sk-...`)
   - Clic en **Add**.
6. Clic en **Deploy**.

Al terminar, Vercel te da una URL tipo:

```
https://estructuras-industriales-mx.vercel.app
```

Ábrela: el sitio carga y el **chat ya responde con el modelo real** (el endpoint
`/api/chat` es del mismo dominio, así que funciona sin más configuración).

## Notas
- **Info que usa el asistente** → variable `SYSTEM_PROMPT` en `api/chat.js`.
- **Rotar la key:** si tu key pasó por un chat o correo, genera una nueva en
  https://platform.deepseek.com y actualiza la variable en Vercel (Settings →
  Environment Variables). Tras cambiarla, haz **Redeploy**.
- **Cada push a `main`** vuelve a desplegar automáticamente.
- **GitHub Pages** sigue funcionando para la parte estática, pero el chat solo
  responde en la versión de **Vercel** (ahí vive la función `/api/chat`).
- **Alternativa Cloudflare Worker:** la carpeta `worker/` tiene la misma lógica por si
  prefieres Cloudflare (ver `worker/README.md`).
