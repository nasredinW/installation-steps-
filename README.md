# installation-steps-
[4:33 PM] Mohamed Bukhris
version: "3"
 
services:

  app:

    container_name: django

    hostname: django_host

    image: ubiaitools/onpremise-be:gpu-v1.7.2

    command: bash /start

    environment:

      - MY_host=0.0.0.0:8000

      - DB_HOST=db

      - DB_NAME=annotation

      - DB_USER=postgres

      - DB_PASS=ubiai

      - DJANGO_SETTINGS_MODULE=Annotation.production

      - CLEAR_MIGRATIONS=no

      - RUN_MAKE_MIGRATIONS=yes

      - RUN_MIGRATION=no

      - TRAIN_CONTAINER_NETWORK=appnet

      - ENABLE_GPU=yes

      - TRAIN_IMAGE=ubiaitools/onpremise-train:v2.4

      - USE_DOCKER=yes

      - TESSDATA_PREFIX=/usr/local/share/tessdata/

      - HOST_HOSTNAME=app

      - HOST_DATASET=$HOME/ubiai_local/backup/Media/dataset

      - HOST_MODEL_STORE=$HOME/ubiai_local/backup/Media/model_store

      - HOST_TRAIN_MODEL=$HOME/ubiai_local/backup/Media/models

    ports:

      - "8000:8000"

      - "8001:8001"

    depends_on:

      - db

      - redis

    volumes:

      - ./ubiai_local/backup/Media:/app/Media:rw

      - ./ubiai_local/backup/Media/models:/app/Media/models:rw

      - ./ubiai_local/backup/Media/dataset:/app/Media/dataset:rw

      - ./ubiai_local/backup/Media/model_store:/app/Media/model_store:rw

      - ./ubiai_local/backup:/app/backup

      - ./ubiai_local/ub/sercret:/app/static/static_server

      - /var/run/docker.sock:/var/run/docker.sock

      - ./ubiai_local/mediafiles/credentials:/app/mediafiles/credentials

      - ./ubiai_local/mediafiles:/app/mediafiles
 
  celery:

    container_name: celery

    restart: always

    image: ubiaitools/onpremise-be:gpu-v1.7.2

    command: celery worker -A Annotation --loglevel=info

    volumes:

      - ./ubiai_local/backup:/app/backup

      - ./ubiai_local/backup/Media:/app/Media:rw

      - ./ubiai_local/backup/Media/models:/app/Media/models:rw

      - ./ubiai_local/backup/Media/dataset:/app/Media/dataset:rw

      - ./ubiai_local/backup/Media/model_store:/app/Media/model_store:rw

      - ./ubiai_local/ub/sercret:/app/static/static_server

      - /var/run/docker.sock:/var/run/docker.sock

      - ./ubiai_local/mediafiles/credentials:/app/mediafiles/credentials

      - ./ubiai_local/mediafiles:/app/mediafiles

    environment:

      - DB_HOST=db

      - DB_NAME=annotation

      - DB_USER=postgres

      - DB_PASS=ubiai

      - RUN_MIGRATION=no

      - DJANGO_SETTINGS_MODULE=Annotation.production

      - TRAIN_CONTAINER_NETWORK=appnet

      - TRAIN_IMAGE=ubiaitools/onpremise-train:v2.4

      - USE_DOCKER=yes

      - ENABLE_GPU=yes

      - TESSDATA_PREFIX=/usr/local/share/tessdata/

      - HOST_HOSTNAME=app

      - HOST_DATASET=$HOME/ubiai_local/backup/Media/dataset

      - HOST_MODEL_STORE=$HOME/ubiai_local/backup/Media/model_store

      - HOST_TRAIN_MODEL=$HOME/ubiai_local/backup/Media/models

    depends_on:

      - db

      - redis
 
  db:

    container_name: db

    restart: always

    image: postgres:latest

    environment:

      - POSTGRES_DB=annotation

      - POSTGRES_USER=postgres

      - POSTGRES_PASSWORD=ubiai

    volumes:

      - ./ubiai_local/backup/db_data:/var/lib/postgresql/data

    ports:

      - 5432:5432
 
  redis:

    container_name: redis

    image: redis:alpine
 
  angular:

    container_name: angular

    image: ubiaitools/onpremise-fe:gpu-v1.10

    ports:

      - "80:80"
 
networks:

  default:

    name: appnet

    external: true

 like 1
[4:35 PM] Mohamed Bukhris
install docker, docker-compose, nvidia driver and nvidia docker runtime
add client to list of Dockerhub collaborators
docker-compose up
activate installation
 
