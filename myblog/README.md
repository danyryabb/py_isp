- new:
- add CI via github actions
- update docker-compose.prod.yml file - django project builds from docker images (all of them are public, check that file)
- update entrypoint.prod - nowadays you need only to run  - docker-compose -f docker-compose.prod.yml up -d --build - from activated venv
- if u have problems with accessing, run -> docker-compose down -> docker-compose down --remove-orphans -> docker-compose -f docker-compose.prod.yml up -d --build
- images: (web) rdany992/myblog_web, (nginx) rdany992/dockerhub:myblog_django_nginx, (postgres) postgres:12.0-alpine.
- previous:
- commit history include all app developing studies
- made 2 async funcs in /personal/views.py - simple objects search - ( ...:1337/async/ | ...:1337/sync/ + console time log (dev mode))
- docker compose for dev/prod mode
- nginx, gunicorn
- postgreSQL
- demo.mov - present project via video
- rdany992/dockerhub - repo on Docker Hub - nginx, db, web apps
- https://hub.docker.com/repository/docker/rdany992/dockerhub
я старался:)
сделать деплой на heroku не получилось, так как сервис он не дружит с docker compose, но можно при желании разделить проект и сделать просто деплой django проекта :) немного не хватило времени доделать все, что хотелось, так как делаю тестовые задания на ios джуна (((
