install:
	poetry install

migrate:
	poetry run python manage.py migrate

lint:
	poetry run pflake8 apps task_manager

run:
	poetry run python manage.py runserver

test:
	poetry run coverage run --source='.' manage.py test

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi:application