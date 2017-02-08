# d-ealer
A Docker Healer - Auto Restarting Unhealthy Containers Edit

# How To

d-ealer will check the health of all of your containers, if one of them is unhealty, it will restart it.

# Configuration

Please adapt the configuration to your need (**d-ealer.conf**):

```
[logging]
logger_level = logging.INFO
handler_level = logging.INFO
log_format = %(asctime)s - %(name)s - %(levelname)s - %(message)s
log_file = d-ealer.log
```

# Logging

You can find logs in ``` d-ealer.log ``` file.
You can mount your log file to your host, if you are using Docker.

# Running d-ealer Using Docker

```
docker run -it --name d-ealer -v /var/run/docker.sock:/var/run/docker.sock  -d eon01/d-ealer
```

# ToDo
- Add the possibility to exclude containers/services from being auto-healed
- Allow users to choose the timeout and retries number ..etc


https://hub.docker.com/r/eon01/d-ealer/
https://github.com/eon01/d-ealer
