# Application server

> This project was on Application servers.

## Summary

I learnt about how to configure a web server to serve dynamic content.
## Files

> Each file contains the solution to a task in the project.

- [x] [2-app_server-nginx_config](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x1A-application_server/2-app_server-nginx_config): `Nginx` config.
- [x] [3-app_server-nginx_config](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x1A-application_server/3-app_server-nginx_config): `Nginx` config.
- [x] [4-app_server-nginx_config](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x1A-application_server/4-app_server-nginx_config): `Nginx` config.
- [x] [5-app_server-nginx_config](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x1A-application_server/5-app_server-nginx_config): `Nginx` config.
- [x] [gunicorn.service](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x1A-application_server/gunicorn.service): A `systemd` script which starts a `Gunicorn` process to serve the same content.
    - The `Gunicorn` process should spawn 3 worker processes
    - The process should log errors in `/tmp/airbnb-error.log`
    - The process should log access in `/tmp/airbnb-access.log`
    - The process should be bound to port `5003`
- [x] [4-reload_gunicorn_no_downtime](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x1A-application_server/4-reload_gunicorn_no_downtime): A simple Bash script to reload Gunicorn in a graceful way.
