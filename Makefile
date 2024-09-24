install:
	poetry install

lint:
	poetry run flake8 apps task_manager

run:
	poetry run python manage.py runserver

test:
	poetry run python ./manage.py test

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi:application