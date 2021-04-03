COMPOSE_FILE=docker-compose.yml

up:
	docker-compose -f $(COMPOSE_FILE) up

build:
	docker-compose -f $(COMPOSE_FILE) build

down:
	docker-compose -f $(COMPOSE_FILE) down

bash:
	docker-compose -f $(COMPOSE_FILE) run --rm backend bash

migrate:
	docker-compose -f $(COMPOSE_FILE) run --rm backend python manage.py migrate

make_migrations:
	docker-compose -f $(COMPOSE_FILE) run --rm backend python manage.py make_migrations

## Code overhaul
mypy:
	docker-compose -f $(COMPOSE_FILE) run --rm backend mypy --config-file .mypy.ini .

flake:
	docker-compose -f $(COMPOSE_FILE) run --rm backend flake8

isort:
	docker-compose -f $(COMPOSE_FILE) run --rm backend isort -rc .

black:
	docker-compose -f $(COMPOSE_FILE) run --rm backend black . --target-version py38 -l 110

supercode: isort black flake mypy