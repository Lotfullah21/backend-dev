## Views

a view is a function designed to handle a web request and return a web response. Each view function takes an HTTP Request object as its first parameter named `request.`

We create the logic inside the views to present the data to the end user.

## 1. Creating URLS

`./home/views.py`
In views, we write our entire logic for page handling

```py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Hi, From django</h1>")

def about(request):
    return HttpResponse("<h2>Hi, from about page</h2>")

def contact(request):
    return HttpResponse("<h3>Hi, from contact page</h3>")
```

In `urls` file, we specify based on which path, which functions from views should be triggered.

`./firstProject/urls.py`

```py
from django.contrib import admin
from django.urls import path
from home.views import index, about, contact

urlpatterns = [
    path("",index,name="index"),
    path("about/",about,name="about"),
    path("contact/",contact,name="contact"),
    path('admin/', admin.site.urls),
]
```

But, the real world application does not contain simple texts, we need to return pages with lots of contents withing it.

To have pages, we create a folder `template` in `home` directory and will be creating pages there.

We use `render(request, page)` to render the given page.

render the whole page in `views.py`

```py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
```

## 2. Navigating to different routes

We can use `href` to navigate to different routes.

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>django|home page</title>
	</head>
	<body>
		<nav style="padding: 4rem">
			<a href="/about">about</a>
			<a href="/contact">contact</a>
		</nav>
		<h1>Welcome to Hooshmandlab</h1>
	</body>
</html>
```

## 3. Dynamic routes

```html
<html lang="en">
	<head>
		<title>django|home page</title>
	</head>
	<body>
		<nav style="padding: 4rem">
			<a href="{%url 'about'%}">about</a>
			<a href="{%url 'contact'%}">contact</a>
		</nav>
	</body>
</html>
```

`<a href="{%url 'about'%}">about</a>`, we are saying that navigate the url based on the name, look for the then name about in urls and navigate to the function or page it rendering.
`path("about/",about,name="about"),`, name should match with what we write after `url` inside `<a>.`

## 4. Creating Dynamic Path

Creating dynamic URLs in Django involves using URL patterns to capture variable parts of a URL and pass them as parameters to your views.

```py
from django.contrib import admin
from django.urls import path
from home.views import index, about, contact, dynamic_url

urlpatterns = [
    path("",index,name="index"),
    path("<id>/", dynamic_url, name="dynamic_url"),
]
```

Now,lets pass the id to views and this is a must.

`./home/views.py`

```py
def dynamic_url(request, id):
    print(f"this is the id= {id}")
    return render(request, "dynamic_url.html")
```

`./home/templates/dynamic_url`

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>Document</title>
	</head>
	<body>
		<nav style="padding: 4rem">
			<a href="{%url 'contact'%}">contact</a>
		</nav>
		<h1>From Dynamic URL</h1>
	</body>
</html>
```

## 5. context

by adding `context` inside render function, we can get access to all the objects that is passed to `context` inside template.

```py
def dynamic_url(request, id):
    print(f"this is the id= {id}")
    return render(request, "dynamic_url.html", context={"id":id, "name":"ahmad"})
```

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>Document</title>
	</head>
	<body>
		<section style="padding: 4rem">
			<nav style="padding: 4rem">
				<a href="{%url 'contact'%}">contact</a>
			</nav>
			<h1>From Dynamic URL</h1>
			<h1>hello {{name}}</h1>
			<h1>id: {{id}}</h1>
		</section>
	</body>
</html>
```

We can pass more than one parameter

```py
path("<id>/<name>/", dynamic_url, name="dynamic_url"),
def dynamic_url(request, id, name):
   print(f"this is the id= {id}")
   return render(request, "dynamic_url.html", context={"id":id, "name":name})

```

When we are navigating to these dynamic url, we have to pass the params we add in path, otherwise it will not work.

## 6. class based views vs function based views

### 1. function based

Function-Based Views in Django are Python functions that take a request and return a response. They are simple and easy to understand for small, straightforward views.

#### Pros:

- Simplicity: Easy to understand, especially for small views.
- Explicitness: Everything is laid out in a single function, making it easier to follow what is happening.
- Flexibility: You can customize the request/response cycle freely without the need for class inheritance.

#### Cons:

- Repetitive Code: For views that share logic (e.g., CRUD operations), you may end up writing repetitive code.
- Limited Scalability: When the view becomes more complex, the function can grow large and become harder to manage.

```py
from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Hello, world!")

```

### 2. class based views

Class-Based Views (CBVs)
Class-Based Views in Django are views organized as Python classes. They provide more structure and built-in functionality, allowing for code reuse and the use of object-oriented patterns.

#### Pros:

- Reusability: You can create reusable and modular components by extending Django's generic views.
- Readability: Logic can be broken down into methods (e.g., get(), post(), delete()), making it easier to organize code, especially for complex views.
- Inheritance: You can take advantage of object-oriented programming (OOP), using inheritance to extend or modify existing views.
- Built-in Generic Views: Django provides many built-in class-based views for common tasks like listing, creating, updating, and deleting objects (CRUD operations).

#### cons

- Complexity: Initially more difficult to understand, especially for beginners.
- Less Explicit: Some logic might be hidden in the class hierarchy, which may require diving into Django's documentation or source code to fully grasp what's happening.

```py
from django.http import HttpResponse
from django.views import View

class MyView(View):
    def get(self, request):
        return HttpResponse("Hello, world!")

```
