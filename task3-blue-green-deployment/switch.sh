#!/bin/bash
TARGET=$1
if [ "$TARGET" != "blue" ] && [ "$TARGET" != "green" ]; then
  echo "Usage: ./switch.sh [blue|green]"
  exit 1
fi

cat << NGINX > nginx.conf
server {
    listen 80;
    location / {
        proxy_pass http://${TARGET}-app:80;
    }
}
NGINX

docker exec bg-router nginx -s reload
UPPER=$(echo "$TARGET" | tr '[:lower:]' '[:upper:]')
echo "[ZERO-DOWNTIME SWITCH] Live traffic routed to: $UPPER environment"
