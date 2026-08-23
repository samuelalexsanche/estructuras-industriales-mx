# Worker de CAABSA STEEL

Un solo Worker atiende dos cosas:

| Ruta | Qué hace |
|------|----------|
| `/` (cualquier otra) | Proxy del asistente de IA (DeepSeek), en streaming |
| `/lead` | Recibe los formularios del sitio y los manda por correo (Resend) |

## Puesta en marcha

```bash
cd worker

# 1) Claves (nunca van en el repo; quedan cifradas en Cloudflare)
npx wrangler secret put DEEPSEEK_API_KEY     # asistente de IA
npx wrangler secret put RESEND_API_KEY       # envío de formularios

# 2) Destinatario: editar LEAD_TO en wrangler.toml

# 3) Publicar
npx wrangler deploy
```

## Correo de los formularios

- `LEAD_TO` — a dónde llegan. Admite varios separados por coma.
- `LEAD_FROM` — remitente. Con el dominio sin verificar se usa el de pruebas de
  Resend. Una vez verificado `caabsasteel.mx` en Resend (dos registros DNS),
  cambiar a `Sitio web CAABSA STEEL <web@caabsasteel.mx>` para que no caiga en
  spam y se vea profesional.
- El `Reply-To` del correo es el del visitante: responder desde el buzón contesta
  directo al prospecto.
- No se guarda nada en el Worker: recibe, envía y responde.

### Protecciones
- Solo acepta peticiones desde los orígenes de `ALLOWED_ORIGINS`.
- Campo trampa oculto (`website`): si viene lleno, se responde `ok` y no se
  envía nada, para no avisarle al bot que fue detectado.
- Valida nombre y formato de correo; recorta los campos largos.

### Prueba rápida (después de desplegar)
```bash
curl -X POST https://estructuras-chat.mattera.workers.dev/lead \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://samuelalexsanche.github.io' \
  -d '{"form":"contacto","nombre":"Prueba","email":"tu@correo.com","telefono":"7225232020","mensaje":"probando"}'
```
