#!/usr/bin/env bash
# hasancan.net yayına alma: depodaki site dosyalarını Caddy'nin sunduğu klasöre kopyalar.
set -euo pipefail
cd "$(dirname "$0")"
rsync -a --delete --exclude '.git' --exclude '.claude' --exclude 'deploy.sh' --exclude 'tools' --exclude '*.md' ./ /var/www/hasancan/
echo "Yayında: https://hasancan.net"
