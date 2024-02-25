# Simple Scaling

To get everything started:

`docker compose up -d --build`

Visit the application at the following end-points:

- ping: `http://localhost/ping`
- news: `http://localhost/news`
- weather: `http://localhost/weather`


Note the ID of the responding container is provided in the "PONG" response.

To scale up the app:

`docker compose up -d --scale app=5 --no-recreate`

To scale it back down the app:

`docker compose up -d --scale app=1 --no-recreate`


To quit the app:

`docker compose down`