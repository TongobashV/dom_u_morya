# Dom U Morya

Django application running with Docker Compose, PostgreSQL and Nginx.

## Architecture

The project consists of three Docker containers:

- Django + Gunicorn — application
- PostgreSQL — database
- Nginx — reverse proxy and static files server

Browser
   |
   v
Nginx :80
   |
   v
Django/Gunicorn :8000
   |
   v
PostgreSQL :5432

Only Nginx is exposed to the host. Django and PostgreSQL are available through the internal Docker network.

## Requirements

- Docker
- Docker Compose

## Project structure

dom_u_morya/
├── Dockerfile
├── docker-compose.yml
├── .env
├── .dockerignore
├── requirements.txt
├── manage.py
├── nginx/
│   └── default.conf
├── staticfiles/
└── ...

## Environment variables

Create a `.env` file in the project root.

Example:

POSTGRES_DB=dom_u_morya
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password

DB_NAME=dom_u_morya
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=postgres
DB_PORT=5432

Do not commit `.env` to Git. Make sure `.env` is included in `.gitignore`.

For a public repository, use `.env.example` with placeholder values.

## Start the project

Build the application image and start all containers:

    docker compose up -d --build

Check status:

    docker compose ps

Open the application:

    http://localhost

## Stop the project

Stop and remove containers:

    docker compose down

Named volumes are preserved.

Start again:

    docker compose up -d

Do NOT use this unless you intentionally want to remove volumes and stored data:

    docker compose down -v

Removing the PostgreSQL volume deletes stored database data.

## Logs

All services:

    docker compose logs

Specific service:

    docker compose logs app
    docker compose logs nginx
    docker compose logs postgres

Follow logs:

    docker compose logs -f app

## Django management commands

Run a Django command inside the app container:

    docker compose exec app python manage.py <command>

Apply migrations:

    docker compose exec app python manage.py migrate

Show migrations:

    docker compose exec app python manage.py showmigrations

Collect static files:

    docker compose exec app python manage.py collectstatic --noinput

Static files are also collected automatically when the app container starts.

## Static files

Static files are stored in the named volume:

    static_volume

The volume is shared between Django and Nginx:

Django
  |
  v
static_volume
  |
  v
Nginx

Nginx serves static files from:

    /var/www/static

Check files inside Nginx:

    docker compose exec nginx find /var/www/static -type f

## PostgreSQL

PostgreSQL data is stored in:

    postgres-data

This named volume allows database data to survive container recreation.

List volumes:

    docker volume ls

Inspect the PostgreSQL volume:

    docker volume inspect dom_u_morya_postgres-data

## Docker network

Services communicate through:

    app-network

Django connects to PostgreSQL using:

    DB_HOST=postgres
    DB_PORT=5432

Nginx connects to Django using:

    app:8000

List networks:

    docker network ls

Inspect the project network:

    docker network inspect dom_u_morya_app-network

## Nginx

Nginx configuration is stored on the host:

    nginx/default.conf

It is bind-mounted into the container:

    ./nginx/default.conf:/etc/nginx/conf.d/default.conf

Nginx acts as a reverse proxy:

Browser
   |
   v
Nginx
   |
   v
Gunicorn
   |
   v
Django

Nginx also serves static files from:

    /var/www/static

## Validate Compose configuration

Validate the Compose file:

    docker compose config

If the configuration is valid, Docker Compose prints the resolved configuration without validation errors.

## Rebuild

Rebuild the application image and recreate services:

    docker compose up -d --build

If only Compose/configuration files changed:

    docker compose up -d

## Execute a shell inside containers

Django:

    docker compose exec app sh

Nginx:

    docker compose exec nginx sh

PostgreSQL:

    docker compose exec postgres sh

## Useful diagnostic commands

Running services:

    docker compose ps

All containers:

    docker compose ps -a

Service logs:

    docker compose logs <service>

Docker networks:

    docker network ls

Inspect network:

    docker network inspect <network_name>

Docker volumes:

    docker volume ls

Inspect volume:

    docker volume inspect <volume_name>

Compose configuration:

    docker compose config

## Typical startup workflow

1. Create `.env`.
2. Validate the Compose configuration:

       docker compose config

3. Build and start the project:

       docker compose up -d --build

4. Check services:

       docker compose ps

5. Check logs if necessary:

       docker compose logs

6. Open:

       http://localhost

## Production-like architecture

Internet / Browser
        |
        v
   Nginx :80
        |
        v
   Django/Gunicorn :8000
        |
        v
   PostgreSQL :5432

Only Nginx is exposed to the host.

Django and PostgreSQL communicate through the internal Docker network.

Database data and static files are stored in Docker named volumes.

## Important notes

- `.env` contains configuration/secrets and must not be committed to Git.
- PostgreSQL data is stored in a named volume.
- Static files are stored in a named volume shared between Django and Nginx.
- `docker compose down` does not remove named volumes.
- `docker compose down -v` removes volumes and can delete database data.
- Nginx is the external entry point.
- Gunicorn and PostgreSQL are not published directly to the host.
