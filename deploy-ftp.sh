#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# CAABSA STEEL — publicar por FTP (cuando el hosting no da SSH)
#
#   ./deploy-ftp.sh          sube solo lo que cambió
#   ./deploy-ftp.sh --dry    muestra qué haría, sin tocar el servidor
#
# La contraseña NO se guarda: se pide en cada ejecución.
# Requiere lftp:  brew install lftp
# ─────────────────────────────────────────────────────────────────────────────
set -euo pipefail
cd "$(dirname "$0")"

command -v lftp >/dev/null || { echo "Falta lftp. Instálalo con:  brew install lftp"; exit 1; }
[ -f deploy.env ] || { echo "Falta deploy.env"; exit 1; }
# shellcheck disable=SC1091
source deploy.env
: "${SSH_USER:?}" "${SSH_HOST:?}"
REMOTE="${FTP_DIR:-public_html}"

DRY=""
if [ "${1:-}" = "--dry" ]; then DRY="--dry-run"; echo "▶ SIMULACRO: no se modifica nada"; fi

echo "▶ Regenerando el sitio…"
python3 _build/gen_site_i18n.py

printf "Contraseña FTP de %s: " "$SSH_USER"
read -rs FTP_PASS; echo

# Lo que nunca se toca: archivos del cliente y del servidor.
EXCL="--exclude-glob _build/ --exclude-glob worker/ --exclude-glob .git/ \
--exclude-glob clientes/ --exclude-glob sgciso/ --exclude-glob sistema/ \
--exclude-glob directorio/ --exclude-glob .well-known/ --exclude-glob cgi-bin/ \
--exclude-glob index.php* --exclude-glob .htaccess.anterior \
--exclude-glob assets/drive-download-*/ --exclude-glob *.md \
--exclude-glob deploy*.sh --exclude-glob deploy.env* --exclude-glob .DS_Store \
--exclude-glob .gitignore --exclude-glob CNAME"

echo "▶ Subiendo a $SSH_HOST:$REMOTE …"
lftp -u "$SSH_USER,$FTP_PASS" "$SSH_HOST" <<LFTP
set ftp:ssl-allow true
set ssl:verify-certificate no
set net:timeout 20
set net:max-retries 3
mirror -R --only-newer --parallel=4 --verbose=1 $DRY $EXCL . $REMOTE
bye
LFTP

[ -n "$DRY" ] && exit 0
echo "▶ Comprobando…"
for u in / /nosotros.html /contacto.html /en/index.html; do
  printf "   %-24s %s\n" "$u" "$(curl -s -o /dev/null -w '%{http_code}' --max-time 15 "https://caabsasteel.mx$u" || echo 000)"
done
echo "▶ Listo."
