# Application Server

This project encompasses various tasks aimed at configuring a web server (nginx) with an application server (Gunicorn).

![c7d1ed0a2e10d1b4e9b3](https://github.com/Official0mega/alx-system_engineering-devops/assets/122806822/6afdaeaf-1d59-4e46-8d6d-49e9a9f9a51d)


## Tasks To Complete

+ [x] 0. Setting Up Development with Python
  - The objective is to serve the code developed for the [AirBnB clone v2 - Web framework](https://github.com/Official0mega/AirBnB_clone_v2) on `web-01`. This task focuses on setting up the development environment, crucial for testing and debugging before production deployment.
  - **Requirements:**
    - Ensure that task #3 of your [SSH project](../0x0B-ssh/README.md) is completed for `web-01` to allow the checker to connect to your servers.
    - Git clone your `AirBnB_clone_v2` on your `web-01` server.
    - Configure the file `web_flask/0-hello_route.py` to serve its content from the route `/airbnb-onepage/` on port `5000`. Your Flask application object must be named `app`.

+ [x] 1. Setting Up Production with Gunicorn
  - Now that the development environment is ready, the task is to set up the production application server with `Gunicorn` on `web-01`, port `5000`. Install `Gunicorn` and any necessary libraries for your application. Your `Flask` application object will act as a [WSGI](https://www.fullstackpython.com/wsgi-servers.html) entry point. The goal is to have the same port for both production and development, ensuring consistent dynamic content serving conditions.
  - **Requirements:**
    - Install `Gunicorn` and any other required libraries.
    - The Flask application object should be called `app`.
    - Serve the same content from the same route as in the previous task. To verify it's working, bind a `Gunicorn` instance to localhost, listening on port `5000`.
    - Ensure that nothing is listening on port `6000`, as the checker will bind a `Gunicorn` instance to port `6000`.

+ [x] 2. Serving a Page with Nginx
  - Building on the previous tasks, configure Nginx to serve your page from the route `/airbnb-onepage/`.
  - **Requirements:**
    - `Nginx` should serve this page both locally and on its public IP on port `80`.
    - Proxy requests to the process listening on port 5000.
    - Include your `Nginx` config file as `2-app_server-nginx_config`.
  - **Notes:**
    - To test this, you may need to spin up your production or development application server (listening on port `5000`).
    - In a production environment, the application server typically starts upon system initialization.

+ [x] 3. Adding a Route with Query Parameters
  - Expanding the web application by adding a service for `Gunicorn` to handle. In `AirBnB_clone_v2/web_flask/6-number_odd_or_even`, the route `/number_odd_or_even/<int:n>` is already defined to render a page indicating whether an integer is odd or even. Configure `Nginx` to proxy HTTP requests to the route `/airbnb-dynamic/number_odd_or_even/(any integer)` to a `Gunicorn` instance on port `5001`.
  - **Requirements:**
    - `Nginx` must serve this page both locally and on its public IP on port `80`.
    - Proxy requests to the route `/airbnb-dynamic/number_odd_or_even/(any integer)` to the process on port `5001`.
    - Include your `Nginx` config file as `3-app_server-nginx_config`.
  - **Tips:**
    - Refer to articles/docs for configuring `Nginx`.
    - To run a `Gunicorn` instance as a detached process, you can use `tmux`.

+ [x] 4. Serving Your API
  - Serve the content from [AirBnB clone v3 - RESTful API](https://github.com/Official0mega/AirBnB_clone_v3) on `web-01`.
  - **Requirements:**
    - Git clone your `AirBnB_clone_v3`.
    - Configure `Nginx` so that the route `/api/` points to a `Gunicorn` instance on port `5002`. Ensure that `Nginx` serves this page locally and on its public IP on port `80`.
    - Bind `Gunicorn` to `api/v1/app.py`. Import data (and environment variables) from [this project](https://github.com/Official0mega/AirBnB_clone_v2).
    - Upload your `Nginx` config file as `4-app_server-nginx_config`.

+ [x] 5. Serving Your AirBnB Clone
  - Serve what you've built for [AirBnB clone - Web dynamic](https://github.com/Official0mega/AirBnB_clone_v4) on `web-01`.
  - **Requirements:**
    - Git clone your [AirBnB_clone_v4](https://github.com/Official0mega/AirBnB_clone_v4).
    - Your `Gunicorn` instance should serve content from web_dynamic/2-hbnb.py on port `5003`.
    - Configure `Nginx` to route `/` to your `Gunicorn` instance.
    - Set up `Nginx` to serve static assets found in `web_dynamic/static/`.
    - Ensure `web_dynamic/static/scripts/2-hbnb.js` is configured with the correct IP.
    - `Nginx` should serve this page both locally and on its public IP on port `5003`.
    - Upload your `Nginx` config as `5-app_server-nginx_config`.

+ [x] 6. Deployment
  - Set up your application server to run by default during Linux boot using `systemd`. This ensures that the `Gunicorn` process starts as part of the system initialization process, eliminating the need for manual restarts.
  - **Requirements:**
    - Write a `systemd` script starting a `Gunicorn` process to serve the same content as in the previous task (`web_dynamic/2-hbnb.py`).
    - The `Gunicorn` process should spawn 3 worker processes.
    - The process should log errors in `/tmp/airbnb-error.log` and access in `/tmp/airbnb-access.log`.
    - Bind the process to port `5003`.
    - Store your `systemd` script in the appropriate directory on `web-01`.
    - Start the systemd service and leave it running.
    - Upload `gunicorn.service` to GitHub.

+ [x] 7. No Service Interruption
  - To maintain uptime, application servers often require restarts to update with new code or configurations, resulting in downtime. To avoid this, a master/workers infrastructure is used. The master is responsible for receiving requests, managing workers (starting, stopping), and distributing requests to workers. Workers process queries and generate dynamic content.
  - Write a Bash script to reload Gunicorn gracefully. This script should be stored in the file [4-reload_gunicorn_no_downtime](4-reload_gunicorn_no_downtime).

