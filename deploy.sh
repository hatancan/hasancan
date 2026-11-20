#!/usr/bin/env bash
# hasancan.net yayına alma: depodaki site dosyalarını Caddy'nin sunduğu klasöre kopyalar.
set -euo pipefail
cd "$(dirname "$0")"
rsync -a --delete --exclude '.git' --exclude '.claude' --exclude 'deploy.sh' --exclude 'tools' --exclude 'api' --exclude '.kilit' --exclude '.gitignore' --exclude 'yazi.md' --exclude '*.md' --exclude '/_g' --exclude '/_b' --exclude '/buzanittin' --exclude '/yolhikayeleri' --exclude '/hidirgoktas' --exclude '/davidmaule' --exclude '/fracinvest' --exclude '/origmark-video-*' --exclude '/dogum-deneme-*' --exclude '/selparteknoloji-sunumu' ./ /var/www/hasancan/
# Kendi şablonunu taşıyan alt sayfaların (Buzanittin vb.) üst menüsünü ana sayfayla eşitle
python3 -I tools/menu_esitle.py /var/www/hasancan
echo "Yayında: https://hasancan.net"
