# Publicar cambios en el sitio

El sitio vive en el hosting del cliente (cPanel de Wingu, `dos2r2063.servwingu.mx`),
carpeta `public_html`. **Nunca se editan los HTML a mano:** se regeneran con
`_build/gen_site_i18n.py` y se sincronizan.

## Primera vez

1. Habilitar SSH en cPanel: **SSH Access → Manage SSH Keys → Generate/Import**, y
   autorizar la llave. En algunos hostings hay que pedirlo por ticket.
2. Copiar `deploy.env.ejemplo` a `deploy.env` y llenar usuario y ruta.
   `deploy.env` está en `.gitignore`: no se sube al repo.
3. Probar la conexión:
   ```bash
   ssh -p 22 USUARIO@dos2r2063.servwingu.mx
   ```

## Cada actualización

```bash
./deploy.sh --dry     # muestra qué cambiaría, sin tocar nada
./deploy.sh           # regenera el sitio y sube solo lo que cambió
```

Sube **solo los archivos modificados**, no los 123 MB. Cambiar un texto suele ser
cuestión de segundos.

## Qué NUNCA toca

`--delete` quita del servidor lo que ya no existe en el proyecto (páginas
renombradas, fotos retiradas), pero estas rutas están excluidas y quedan intactas:

| Ruta | Por qué |
|------|---------|
| `clientes/`, `directorio/`, `sgciso/`, `sistema/` | Sistemas internos del cliente |
| `.well-known/` | Validación del certificado SSL |
| `google*.html` | Verificación de Google Search Console |
| `index.php*` | Su sitio anterior, conservado por si hay que volver |
| `.git/`, `cgi-bin/` | Del servidor |

Comprobado con `rsync --dry-run` contra una copia de la estructura real: **cero
operaciones de borrado** sobre archivos del cliente.

## Si no hay SSH

Alternativa por FTP, que también sube solo lo cambiado:

```bash
brew install lftp
lftp -u USUARIO,CONTRASEÑA dos2r2063.servwingu.mx -e \
  "mirror -R --only-newer --parallel=4 \
   --exclude-glob _build/ --exclude-glob worker/ --exclude-glob .git/ \
   --exclude-glob clientes/ --exclude-glob sgciso/ --exclude-glob sistema/ \
   --exclude-glob directorio/ --exclude-glob .well-known/ \
   . public_html; quit"
```

Sin `--delete`, por seguridad: con FTP conviene borrar a mano lo que sobre.

## El Worker es aparte

El asistente de IA y el envío de formularios viven en Cloudflare, no en el
hosting. Se despliegan por su cuenta:

```bash
cd worker && npx wrangler deploy
```
