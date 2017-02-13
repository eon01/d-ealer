# Testing D-ealer With A Healthcheck

This test uses this [repository](https://github.com/tomwillfixit/healthcheck) Dockerfile in order to create a container having a healthcheck.


To test it, build it:

```
docker build -t helloworld:healthcheck .
```

Run it:

```
docker run -l com.dealer.activate=1 -d -P helloworld:healthcheck
```

Make sure the .bin file is executable ( ``` chmod +x ``` otherwise).

```
CONTAINER ID        IMAGE                    COMMAND             CREATED             STATUS                    PORTS                   NAMES
a79307e481b5        helloworld:healthcheck   "/helloworld.bin"   47 seconds ago      Up 46 seconds (healthy)   0.0.0.0:32769->80/tcp   dazzling_brattain
```



