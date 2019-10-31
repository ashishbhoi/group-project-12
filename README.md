# group-project-12 #

Django Group Project For Data Base and Information System Lab

## Step To Configure Project ##

### Create a new python virtual env for your project ###
    virtualenv venv

### Activate python virtual env for your project ###
    source venv/bin/activate

### Install all required dependency ###
    pip install -r requirements.txt

## How to run The application ##

### Make Migrations ###
    python manage.py makemigrations

### Migrate Relations To Database ###
    python manage.py migrate

### Collect Static ###
    python manage.py collectstatic

### Run Live Server Locally ###
    python manage.py runserver
