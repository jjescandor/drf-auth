## LAB - Class 33

#### Project: Django Authentication & Production Server
#### Author: JJ Escandor

#### Description
 - This is project introduces Django Rest Framework, Docker, Postgresql

### Run the app
 - source .venv/bin/activate
 - docker compose up -d
 - go to http://0.0.0.0:8000/api/token/ in the browser
 - admin username: code01 password: ASDFzxcv!@34 

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
1. In order to run the test, go to settings.py, comment in the Database entry for sqlite3
1. Comment out database entry for posgtresql
1. run python3 manage.py test in the browser
