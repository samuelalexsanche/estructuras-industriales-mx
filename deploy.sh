#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# CAABSA STEEL — publicar el sitio en el hosting (cPanel)
#
#   ./deploy.sh            sube solo lo que cambió
#   ./deploy.sh --dry      muestra qué haría, sin tocar el servidor
#
# Configura una vez tus datos en deploy.env (no se sube a git):
#   SSH_USER=usuariodelcpanel
#   SSH_HOST=dos2r2063.servwingu.mx
#   SSH_PORT=22
#   REMOTE_DIR=/home/usuariodelcpanel/public_html
# ─────────────────────────────────────────────────────────────────────────────
set -euo pipefail
cd "$(dirname "$0")"

[ -f deploy.env ] || { echo "Falta deploy.env — copia deploy.env.ejemplo y llénalo."; exit 1; }
# shellcheck disable=SC1091
source deploy.env
: "${SSH_USER:?}" "${SSH_HOST:?}" "${REMOTE_DIR:?}"
SSH_PORT="${SSH_PORT:-22}"

DRY=""
[ "${1:-}" = "--dry" ] && DRY="--dry-run" && echo "▶ SIMULACRO: no se modifica nada en el servidor"

echo "▶ Regenerando el sitio…"
python3 _build/gen_site_i18n.py

echo "▶ Sincronizando con $SSH_HOST…"
# --delete quita del servidor lo que ya no existe aquí (páginas renombradas, fotos
# retiradas). Los --exclude de abajo son lo que NUNCA se toca: archivos del
# cliente y del servidor que no forman parte de este sitio.
rsync -az --stats $DRY \
  --delete \
  --exclude '.git/' \
  --exclude '.well-known/' \
  --exclude 'google*.html' \
  --exclude 'cgi-bin/' \
  --exclude 'clientes/' \
  --exclude 'directorio/' \
  --exclude 'sgciso/' \
  --exclude 'sistema/' \
  --exclude 'index.php*' \
  --exclude '.htaccess.anterior' \
  --exclude '_build/' \
  --exclude 'worker/' \
  --exclude 'assets/drive-download-*/' \
  --exclude '*.md' \
  --exclude 'deploy.sh' \
  --exclude 'deploy.env*' \
  --exclude '.gitignore' \
  --exclude '.DS_Store' \
  -e "ssh -p $SSH_PORT" \
  ./ "$SSH_USER@$SSH_HOST:$REMOTE_DIR/"

[ -n "$DRY" ] && exit 0

echo "▶ Comprobando el sitio…"
for u in / /nosotros.html /contacto.html /sectores/automotriz.html /en/index.html; do
  code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 15 "https://caabsasteel.mx$u" || echo 000)
  printf "   %-32s %s\n" "$u" "$code"
done
echo "▶ Listo."
