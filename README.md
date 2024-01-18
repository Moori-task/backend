## Project setup

### Production
change the settings in manage.py to production.
```
docker-compose -f docker-compose.production.yaml up --build
```
### Development
change the settings in manage.py to production.

then bring up postgres using docker-compose with below command:
```
docker-compose -f docker-compose.development.yaml up --build
```
after that run django server locally using below command:
```
./manage.py runserver
```
