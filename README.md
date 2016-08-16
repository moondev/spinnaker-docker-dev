# spinnaker-docker-dev

clone sources and substitute configs from config folder
```
python clone.py
```

start services
```
docker-compose up
```

restart a service (code or config change)
```
docker-compose clouddriver restart
```

stop all services
```
docker-compose down
```