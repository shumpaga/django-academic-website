run:
	python manage.py runserver

venv:
	virtualenv --python=python3.6 academic-virtualenv

shell:
	python manage.py shell

install:
	pip install django~=1.10.0
	pip install django-dbbackup
	pip install django-ckeditor
	pip install django-embed-video
	pip install psycopg2
	pip install image
	pip install django-threadedcomments
	pip install matplotlib
	python manage.py migrate

notify-database:
	python manage.py makemigrations
	python manage.py migrate

update-static-files:
	python manage.py collectstatic

create-super-user:
	python manage.py createsuperuser

send-newsletter:
	python manage.py send_newsletter

backup:
	python manage.py dbbackup
	python manage.py mediabackup

.PHONY: notify-database run create-super-user venv backup
