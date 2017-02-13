# d-ealer
A Docker Healer - Auto Restarting Unhealthy Containers

# How To

d-ealer will check the health of all of your containers, if one of them is unhealty, it will restart it.

d-ealer will only restart containers having the label ``` com.dealer.activate ``` set to ``` 1 ```.

This is an example:

```
docker run -l com.dealer.activate=1 -d -P helloworld:healthcheck
```


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

# Common Problems:

## 'module' object has on attribute 'connection' 

This is an issue in docker-py, for me it was solved by:

```
pip install urllib3==1.14
export PYTHONPATH=/usr/local/lib/python2.7/dist-packages:/usr/lib/python2.7/dist-packages
```

On docker-py github issues, other people solved this by:

```
apt-get install python-openssl
```

or

```
sudo pip install --upgrade pip
```


# ToDo
- Allow users to choose the timeout and retries number ..etc

# Links

- Docker Hub: https://hub.docker.com/r/eon01/d-ealer/
- GitHub : https://github.com/eon01/d-ealer
