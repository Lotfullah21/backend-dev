from django.shortcuts import render
from django.http import HttpResponse


def courses(request):
    return HttpResponse("All courses")

def get_path(request):
    path = request.path
    return HttpResponse(path, content_type="text/html",charset="utf-8")

def get_user_info(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META["REMOTE_ADDR"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path_info = request.path_info
    
    message = f"""
    
    Path: {path}<br>
    Scheme: {scheme}<br>
    Method: {method}<br>
    Address: {address}<br>
    User Agent: {user_agent}<br>
    Path Info: {path_info}<br>
    
    """
    return HttpResponse(message)

def get_course_path_info(request,name, id):
    return HttpResponse(f"course {name}  has id number: {id}")

def get_course_query_string(request):
    name = request.GET["name"]
    id = request.GET["id"]
    return HttpResponse(f"course {name}  has id number: {id}")

def show_form(request):
    return render(request, "form.html")


def capture_form(request):
    if request.method == "POST":
        id = request.POST["id"]
        name = request.POST["name"]
    return HttpResponse(f"name: {name} id: {id}")

