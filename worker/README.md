# Worker de CAABSA STEEL

Un solo Worker atiende dos cosas:

| Ruta | Qué hace |
|------|----------|
| `/` (cualquier otra) | Proxy del asistente de IA (DeepSeek), en streaming |
| `/lead` | Recibe los formularios del sitio y los manda por correo (Resend) |

## Puesta en marcha

```bash
cd worker

# 1) Secretos (nunca van en el repo; quedan cifrados en Cloudflare)
npx wrangler secret put DEEPSEEK_API_KEY     # asistente de IA
npx wrangler secret put RESEND_API_KEY       # envío de formularios
npx wrangler secret put LEAD_TO              # a dónde llegan los formularios

# 2) Publicar
npx wrangler deploy
```

> `LEAD_TO` va como secreto y no como variable porque **este repositorio es
> público**: un correo escrito en `wrangler.toml` quedaría a la vista de los
> rastreadores de spam. Admite varios separados por coma.

## Correo de los formularios

- `LEAD_TO` — a dónde llegan (secreto). Admite varios separados por coma.

### Modo de pruebas de Resend
Mientras no haya un dominio verificado, Resend **solo entrega al correo de la
cuenta** y responde 403 `validation_error` para cualquier otro destinatario.
Para probar de punta a punta antes de tener el dominio, pon tu propio correo en
`LEAD_TO`. Al verificar el dominio en resend.com/domains (dos registros DNS) se
levanta la restricción y `LEAD_FROM` pasa a `web@caabsasteel.mx`.
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
