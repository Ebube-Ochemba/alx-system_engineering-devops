# Web stack debugging #4

> This project about more Web stack debugging cases.

## Summary

I learnt about debugging our web stack using `ApacheBench` for benchmark tests and how to improve our performance. These an overview of the steps I took for the project (Task #0).
- Run benchmark test: `ab -c 100 -n 2000 localhost/`
  - Optional: use `tmux` and split the terminal window into two panes and monitor memory and CPU usage in one terminal while you run benchmark in another terminal.
- **Understand the Benchmark Results**:
  - Failed Requests: `xxx` out of `xxxx` requests failed.
  - Non-2xx Responses: `xxxx` responses were not in the 200-299 range, indicating many requests did not succeed.
- **Examine Logs**:
  - Access Logs: These logs show details of all incoming requests.
    - `sudo tail -n 100 /var/log/nginx/access.log`
  - Error Logs: These logs show any errors Nginx encountered while handling requests.
    - `sudo tail -n 100 /var/log/nginx/error.log`
- **Check System Resource Usage**:
  - CPU Usage: `top` or `htop`
  - Memory Usage: `free -m`
  - Disk Usage: `df -h`
> At this point, the error logs, indicated that the Nginx server was hitting the limit for the number of "open files":
```sh
root@69d6aeb63cf8:/# sudo tail -n 100 /var/log/nginx/error.log
2024/06/20 16:09:52 [crit] 35#0: *5940 open() "/usr/share/nginx/html/index.html" failed (24: Too many open files), client: 127.0.0.1, server: localhost, request: "GET / HTTP/1.0", host: "localhost"
2024/06/20 16:09:52 [crit] 35#0: accept4() failed (24: Too many open files)
...
2024/06/20 16:09:52 [crit] 33#0: *6000 open() "/usr/share/nginx/html/index.html" failed (24: Too many open files), client: 127.0.0.1, server: localhost, request: "GET / HTTP/1.0", host: "localhost"
2024/06/20 16:09:52 [crit] 35#0: accept4() failed (24: Too many open files)
2024/06/20 16:09:52 [crit] 35#0: accept4() failed (24: Too many open files)
2024/06/20 16:09:52 [crit] 35#0: accept4() failed (24: Too many open files)
```
> This was causing the server to be unable to accept new connections and serve files, which explains the high number of failed requests. (`873 out of 2000`).

- **Review Nginx Configuration**:
  - First check the current limits: `ulimit -a` or `ulimit -n`
    - This value is associated with the *soft limit*. It can be adjusted by the current user within the constraints of the *hard limit*. See `/etc/security/limits.conf`.
  - Then edit/update the Nginx Configuration File appropriately: `/etc/default/nginx`
    - update `ULIMIT="-n xxx"` to a value that is high enough to accommodate the number of failed requests, but not higher than the *hard limit*. (from `15` to `4096`)
  - Restart Nginx: `service nginx restart`

## Files

> Each file contains the solution to a task in the project.

- [x] [0-the_sky_is_the_limit_not.pp](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/tree/master/0x1B-web_stack_debugging_4/0-the_sky_is_the_limit_not.pp): In this case, I will make 2000 requests to my server with 100 requests at a time. We can see that 943 requests failed, let’s fix our stack so that we get to 0.
- [x] [1-user_limit.pp](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/tree/master/0x1B-web_stack_debugging_4/1-user_limit.pp): Change the OS configuration so that it is possible to login with the `holberton` user and open a file without any error message.