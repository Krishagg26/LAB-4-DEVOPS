#!/bin/bash
W_STABLE=$1
W_CANARY=$2

if [ "$W_STABLE" -eq 0 ]; then
  UPSTREAM="server canary-v2:80;"
elif [ "$W_CANARY" -eq 0 ]; then
  UPSTREAM="server stable-v1:80;"
else
  UPSTREAM="server stable-v1:80 weight=${W_STABLE};
    server canary-v2:80 weight=${W_CANARY};"
fi

cat << NGINX > nginx.conf
upstream app_cluster {
    ${UPSTREAM}
}
server {
    listen 80;
    location / {
        proxy_pass http://app_cluster;
    }
}
NGINX

docker exec canary-router nginx -s reload
echo "[ROLLOUT WEIGHTS UPDATED] Stable v1 weight=${W_STABLE} | Canary v2 weight=${W_CANARY}"
