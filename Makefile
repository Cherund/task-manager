install:
	poetry install

lint:
	poetry run flake8 task_manager

run:
	poetry run python manage.py runserver

