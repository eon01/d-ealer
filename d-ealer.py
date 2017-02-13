import docker
import logging
import traceback
import ConfigParser
import time

# start configuration parser
parser = ConfigParser.ConfigParser()
parser.read("d-ealer.conf")

# reading variables
logger_level = parser.get('logging', 'logger_level', raw = True)
handler_level = parser.get('logging', 'handler_level', raw = True)
log_format = parser.get('logging', 'log_format', raw = True)
log_file = parser.get('logging', 'log_file')

# set logger logging level
logger = logging.getLogger(__name__)
logger.setLevel(eval(logger_level))

# set handler logging level
handler = logging.FileHandler(log_file)
handler.setLevel(eval(handler_level))

# create a logging format
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

def dealer(containers, s):
    for container in containers:
        try:
            label_check = container.attrs['Config']['Labels']['com.dealer.activate']
        except KeyError:
            pass
        if label_check == 1:
    	    try:
                healthcheck = container.attrs['State']['Health']['Status']

        	if healthcheck == "unhealthy":
        	    container.restart()
        	else:
        	    print healthcheck
        	    pass
            except KeyError:
        	logger.error('healthcheck disabled on container %s. Passing' % container.name)
        	pass
            except:
    	        logger.error('Unkown problem on container %s : %s. Please check Docker logs. Passing' % traceback.format_exc(),container.name)
    	        pass
    time.sleep(s)
    return

if __name__ == "__main__":
    # start docker cli
    client = docker.from_env()
    containers = client.containers.list()

    s = 1

    # check healthchecks and restart
    while True:
        dealer(containers, s)


