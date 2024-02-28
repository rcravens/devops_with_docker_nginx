#!/bin/sh

# get current symlink
current=$(docker compose exec nginx ls -la /etc/nginx/nginx.conf)
#echo $current

# echo out the production deployment
if [[ $current = *"green"* ]]; then
  echo "production is GREEN"
else
  echo "production is BLUE"
fi
