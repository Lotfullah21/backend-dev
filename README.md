# Django Project Documentation

## Overview

This repository contains documentation about a Django project, guiding users on how to create a Django app, detailing the files it contains, and providing a comprehensive detail of each part of a Django application.

## Related Documents

- [django](./firstProject/documents/intro-django/README.md)
- [server](./firstProject/documents/server/README.md)
- [views](./firstProject/documents/view/README.md)
- [url](./firstProject/documents/url/README.md)
- [database](./firstProject/documents/database/README.md)
- [model](./firstProject/documents/model/README.md)
- [model-relationships](./firstProject/documents/model/RELATIONSHIPS.md)
- [model-schema](./firstProject/documents/model/MODELSCHEMA.md)
- [related_name](./firstProject/documents/model/RLEATED_NAME.md)
- [migrations](./firstProject/documents/model/MIGRATIONS.md)
- [save-method](./firstProject/documents/model/SAVEMETHOD.md)
- [architecture](./firstProject/documents/architecture/README.md)
- [template](./firstProject/documents/tempalte/README.md)

firstProject/documents/model/RELATIONSHIPS.md

## 1. Technologies Used

- **Backend and Frontend**: Django (with Django templates for frontend rendering)
- **Database**: PostgreSQL
- **Authentication**: Django's built-in authentication system
- **UI Framework**: Bootstrap (for styling)
- **Database ORM**: Django ORM

## 2. Project Structure

Here is the high-level folder structure for the project:

```bash
firstProject/
├── manage.py
├── firstProject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py

├── home/
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

## Setup for the project

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
