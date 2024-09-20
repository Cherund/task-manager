install:
	poetry install

lint:
	poetry run flake8 apps task_manager

run:
	poetry run python manage.py runserver

