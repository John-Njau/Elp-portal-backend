serve:
	python3 manage.py runserver

migrations:
	python3 manage.py makemigrations
	python3 manage.py migrate

superuser:
	python3 manage.py createsuperuser

requirements:
	python3 -m pip install -r requirements.txt

test:
	python3 manage.py test

flush:
	python3 manage.py flush

rmmigrations:
	rm -rfv ./*/migrations/!(__init__.py)

syncdb:
	python3 manage.py migrate --run-syncdb

showmigrations:
	python3 manage.py showmigrations