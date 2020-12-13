ifndef ENV
ENV = dev
endif

DJANGO_PROJECT_DIR=santa_workshop

init:
	poetry config virtualenvs.in-project true --local
	poetry config virtualenvs.create true --local
	poetry init
	poetry env use python3.9

install:
	poetry install

setup: init activate install

db:
	mkdir -p data
	docker volume create data
	docker run \
		-it \
		--rm \
		--network=host \
		--name=webinar1_postgres \
		--volume=data:/var/lib/postgresql/data \
		-e POSTGRES_PASSWORD=mysecretpassword \
		postgres:13

manage:
	ENV=$(ENV) \
	poetry run python $(DJANGO_PROJECT_DIR)/manage.py $(MANAGE_EXEC)

run: MANAGE_EXEC=runserver
run: manage

migrate: MANAGE_EXEC=migrate
migrate: manage

migrations: MANAGE_EXEC=makemigrations
migrations: manage