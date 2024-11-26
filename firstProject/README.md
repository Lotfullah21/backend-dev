# Django Project Documentation

## Reading Documents

- [django](./documents/intro-django/README.md)
- [server](./documents/server/README.md)
- [architecture](./documents/architecture/README.md)
- [url](./documents/url/README.md)
- [views](./documents/view/README.md)
- [database](./documents/database/README.md)
- [model](./documents/model/README.md)
- [ORM](./documents/model/ORM.md)
- [model-relationships](./documents/model/RELATIONSHIPS.md)
- [model-schema](./documents/model/MODELSCHEMA.md)
- [related_name](./documents/model/RLEATED_NAME.md)
- [save-method](./documents/model/SAVEMETHOD.md)
- [template](./documents/tempalte/README.md)

## Overview

This repository contains documentation about a Django project, guiding users on how to create a Django app, detailing the files it contains, and providing a comprehensive detail of each part of a Django application.

## How to start with the project

```sh
# install python and pip using Homebrew
brew install python

# install virtualenv using pip
python3 -m pip install virtualenv

# make a main directory
mkdir directory_name
cd directory_name

# create a new virtual environment
virtualenv env

# activate virtual environment (macOS)
source env/bin/activate

# add .gitignore and requirements.txt
touch .gitignore
touch requirements.txt

# install Django in the virtual environment
pip install django
pip install python-dotenv

# check if Django is installed
django-admin --version
#
pip install -r requirements.txt
# create a new Django project (corrected command)
django-admin startproject project_name

# go to the project directory
cd project_name

# create an app inside the project
django-admin startapp appname
# or
python manage.py startapp appname

# start the development server
python manage.py runserver
```

## 1. Technologies Used

- **Backend and Frontend**: Django (with Django templates for frontend rendering)
- **Database**: PostgreSQL
- **Authentication**: Django's built-in authentication system
- **UI Framework**: Bootstrap (for styling)
- **Database ORM**: Django ORM

## 2. Project Structure

Here is the high-level folder structure for the project:

```bash

├── manage.py
├──
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py

├── home/  # Course-related logic
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── docs/
│
├── README.md
└── .gitignore

```
