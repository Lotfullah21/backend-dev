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

## servers

servers are computers that runs applications and services.
It provides service to the use and another computer.
They are stored in data centers, all of the servers are connected to the internet and running different applications.

Data centers are built based on the service purpose, for instance if it provides more content like images and videos, it will have more hard drive space.
these devices are called ` hardware` and the piece of code that run on them are known as `software`.

```py
# Step 1: Activate the virtual environment
source env/bin/activate

# Step 2: Change to your Django project directory
cd firstProject

# Step 3: Run the development server
python manage.py runserver
```

```sh
<!-- to stop or remove a file from already committed file to github. -->
git rm -r --cached path/to/media/directory
```

## web server

a web server commonly do the following tasks.

- website storage and administration
- data storage
- security
- managing emails
- responding ot web requests from the client

## webpage

a webpage is a document that displays image, videos, text and various content, it is a single page.

## website

a website is collection of webpages that are linked together.

## web application

web applications are more interactive where websites are more informative like `wikipedia`.

## page rendering

when the server sends the page content, the process of reading the code and creating the page on the screen is known page rendering.

## browser

It is a software that allows us to browse on world wide web.

## HTTP

a protocol that is used between the client(user) and the server.
it is used to transfer web resources like images, HTML, videos and so on.

## Library

A library supplies reusable pieces of code that we can use in our application instead of having to re-create the required code.
they are built for a specific purpose.
For instance a library for validating the emails.

## Framework

Frameworks provides the blueprint or structure to work with.
It defines flow and control of our application.

#### Advantages

- time saving
- structure
- best practices

in frameworks, we are having more freedom.

## API

application program interfaces that allows us to interact with an application.
