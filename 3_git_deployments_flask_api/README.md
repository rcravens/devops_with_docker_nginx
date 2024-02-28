# Git Deployments

For this example we are using another Github repo as the source for our code:

[Github Repo - Flask API Example](https://github.com/rcravens/flask_api_example)

This example build on a previous Blue/Green deployment work. In this case, we are using git commands to pull code into
the docker containers. Note that this repo has the following tagged version:

- v1
- v2
- v3

The only difference in these versions is the value set for the `_version` element in the json result.

### Configuration

First copy and rename the `app/.env_example` file to `app/.env`. Then go to the two organizations and get API keys if
you want the news and weather end-points to work.

Second copy the `.env_example` to `.env`. The defaults in this file should be good to deploy version 1 of the example
app to both BLUE & GREEN containers.

### Initial Deployment

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

### Stage And Deploy A New Version

The versions deployed to the Blue/Green containers is controlled by the values in the `.env` file:

- `APP_VERSION_GREEN` sets the version in the Green container
- `APP_VERSION_BLUE` sets the version in the Blue container

Valid values are "v1", "v2", or "v3" and these are the tags on the master branch for the release

The "staging server" is the one that is not being served up by Nginx at `http://localhost/ping`.
To update the version on the staging server do the following:

1. `./which_is_production.sh` to determine which color is currently production
2. Update the version in the `.env` file for the staging server (not production)
3. `./stage_version.sh` to reload the staging server with the new version
4. If needed, use the command below to scale staging
5. `./swap_deploy.sh` to swap this new version into production. Note that you can run the command again to sway back.

### Scaling

Also, not that each version (BLUE/GREEN) can be scaled up individually using:

`docker compose up -d --scale app_blue=5 --no-recreate`

or

`docker compose up -d --scale app_green=5 --no-recreate`

To scale it back down the app:

`docker compose up -d --scale app_blue=1 --no-recreate`

or

`docker compose up -d --scale app_green=1 --no-recreate`

### Shutting Down The Servers

To quit the app there are a few options:

- `docker compose down app_blue` - stops the BLUE app
- `docker compose down app_green` - stops the GREEN app
- `docker compose down` - stops all applications and nginx

You can also start / build individual apps:

- `docker compose up -d --build app_blue` - starts BLUE app with optional `--build` directive
- `docker compose up -d --build app_green` - starts GREEN app with optional `--build` directive
