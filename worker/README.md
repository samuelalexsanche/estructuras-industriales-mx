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
- `SITE_URL` — de dónde toma el correo el logotipo del membrete.
- No se guarda nada en el Worker: recibe, envía y responde.

### Diseño del correo
El aviso llega con el membrete de CAABSA STEEL: barra azul marino con el
logotipo, distintivo de color según el tipo de contacto (Cliente, Proveedor,
Empleo o Descarga de brochure), botones de **Responder / WhatsApp / Llamar**,
la ficha de datos en tabla y el mensaje en bloque citado. Maquetado con tablas
y estilos en línea, que es lo único que respetan Outlook, Gmail y Apple Mail por
igual, y con versión en texto plano para clientes que no muestran HTML.

Para verlo sin desplegar nada:
```bash
node /tmp/preview.mjs     # genera _mail_contacto.html y _mail_brochure.html
```

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
