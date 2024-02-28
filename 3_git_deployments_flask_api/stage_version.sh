#!/bin/sh

# get .env file as bash variables
source .env
#echo "git repo url=${GIT_REPO_URL}"

# get current symlink
current=$(docker compose exec nginx ls -la /etc/nginx/nginx.conf)
#echo $current

# conditionally stage to the "non-production" color
#   Note: if you previously scaled up, this will scale back down to a single instance
if [[ $current = *"green"* ]]; then
  echo "staging ${APP_VERSION_BLUE} to BLUE"
  docker compose up -d --build app_blue
else
  echo "staging ${APP_VERSION_GREEN} to GREEN"
  docker compose up -d --build app_green
fi
