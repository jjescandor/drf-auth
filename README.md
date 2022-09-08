## LAB - Class 33

#### Project: Django Authentication & Production Server
#### Author: JJ Escandor

#### Description
 - This is project introduces Django Rest Framework, Docker, Postgresql, JWT

### To get tokens
 - source .venv/bin/activate
 - docker compose up -d
 - go to http://0.0.0.0:8000/api/token/ in the browser
 - admin username: code01 password: ASDFzxcv!@34 


### Test in Thunderclient
1. Make a new Thunderclient request to: http://0.0.0.0:8000/api/v1/evcars
1. Select Auth tab
1. Select Bearer and in the field, input your token
1. Click Send

### Features - Django
- Add JWT Authentication to your API.
- Install needed libraries in project configuration and/or site settings.
- Keep any pre-existing authentication so DRF Browsable API still usable.
- Install needed libraries in project configuration and/or site settings.
### Features - Docker
- Switch to using Gunicorn instead of Django’s built in development server.
- Mind the number of workers to avoid sluggishness
- Warning You will run into styling issues when you switch over to Gunicorn.
- On Django side you’ll need to properly handle static files using Whitenoise
### Storage Options
- Your choice of SQLite or PostgreSQL.
- Adjust docker-compose.yml so that data is persisted in a volume outside of container.
- These steps are different depending on whether SQLite or PostgreSQL is being used.


### Tests
1. run docker compose run web python3 manage.py test


