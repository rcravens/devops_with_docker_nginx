# Blue / Green Deployments

To get everything started:

`docker compose up -d --build`

Visit the application at the following **production** end-points:

- ping: `http://localhost/ping`
- news: `http://localhost/news`
- weather: `http://localhost/weather`

Visit each version of the application at the following **non-production** end-points:

- ping: `http://localhost/green/ping`
- news: `http://localhost/green/news`
- weather: `http://localhost/green/weather`

- ping: `http://localhost/blue/ping`
- news: `http://localhost/blue/news`
- weather: `http://localhost/blue/weather`

To switch the deployment between the BLUE or GREEN versions of the applications, run the following script:

`./swap_deploy.sh`


Also, not that each version (BLUE/GREEN) can be scaled up individually using:


`docker compose up -d --scale app_blue=5 --no-recreate`

or

`docker compose up -d --scale app_green=5 --no-recreate`


To scale it back down the app:

`docker compose up -d --scale app_blue=1 --no-recreate`

or

`docker compose up -d --scale app_green=1 --no-recreate`

To quit the app there are a few options:

- `docker compose down app_blue` - stops the BLUE app
- `docker compose down app_green` - stops the GREEN app
- `docker compose down` - stops all applications and nginx

You can also start / build individual apps:
- `docker compose up -d --build app_blue` - starts BLUE app with optional `--build` directive
- `docker compose up -d --build app_green` - starts GREEN app with optional `--build` directive
