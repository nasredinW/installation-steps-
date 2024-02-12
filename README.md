# Project Name

Brief description of the project.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
  - [Django (app) Service](#django-app-service)
  - [Celery Service](#celery-service)
  - [PostgreSQL (db) Service](#postgresql-db-service)
  - [Redis Service](#redis-service)
  - [Angular Service](#angular-service)
- [Networks](#networks)

## Overview

This repository contains the Docker Compose configuration for deploying the UbiaiTools OnPremise application with GPU support. The setup includes services for the Django backend (app), Celery for background tasks, PostgreSQL as the database (db), Redis for caching, and an Angular frontend.

## Prerequisites

Before you start the installation process, make sure you have the following software installed on your machine:

- Docker
- Docker Compose
- NVIDIA driver
- NVIDIA Docker runtime

Additionally, ensure that your DockerHub account is added to the list of collaborators for the required images.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Run Docker Compose:

    ```bash
    docker-compose up
    ```

3. Activate Installation:

    Follow the activation steps provided by the UbiaiTools OnPremise application.

## Configuration

### Django (app) Service

The Django service is the main backend for the UbiaiTools OnPremise application. It utilizes the `ubiaitools/onpremise-be:gpu-v1.7.2` image.

- **Environment Variables:**
  - `MY_host`: Host address and port for Django (default: 0.0.0.0:8000)
  - ...

- **Ports:**
  - 8000:8000 (Django app)
  - 8001:8001 (Additional port)

- **Volumes:**
  - ...

### Celery Service

The Celery service is responsible for handling background tasks using the `ubiaitools/onpremise-be:gpu-v1.7.2` image.

- **Environment Variables:**
  - ...

- **Volumes:**
  - ...

- **Depends On:**
  - db
  - redis

### PostgreSQL (db) Service

The PostgreSQL service uses the official `postgres:latest` image.

- **Environment Variables:**
  - ...

- **Volumes:**
  - ...

- **Ports:**
  - 5432:5432

### Redis Service

The Redis service uses the official `redis:alpine` image.

### Angular Service

The Angular service is the frontend of the UbiaiTools OnPremise application, using the `ubiaitools/onpremise-fe:gpu-v1.10` image.

- **Ports:**
  - 80:80

## Networks

The Docker Compose setup uses an external network named `appnet`.

---

Feel free to adjust the configuration as needed for your specific environment and requirements.
