# spinnaker-docker-dev
Requires docker

Ensure you have at least 2 cpus and 6gb of memory provisioned in your docker settings

## Step 1: Fill out our aws secret and key inside .env

## Step : clones sources and swaps configs and builds deck in a temporary container
```
python clone.py
```

## Step 3: start all services (they will take a bit of time to build for the first time)
```
python start_all.py
```

When services finish building deck will be available on localhost:9000

All code is available to edit in the services folder, once you make a change you just need to restart the individual service

restart a service (code or config change)
```
docker-compose restart clouddriver
```

stop all services
```
docker-compose down
```
