from django.shortcuts import render, redirect
from home.forms import ContactForm
from home.models import ContactModel
import random
# Create your views here.



def index(request):  
    courses = ["ai","js","dl","css","html"]
    age =0
    num = random.randint(10, 1000)
    return render(request,"index.html", context={"random_number":num, "courses":courses, "age":age})

def about(request):
    return render(request, "about.html")

def contact(request):

    if request.method=="POST":
        # get the info from posted request
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            contact = ContactModel(**form.cleaned_data)
            contact.save()
            return redirect("/contact/")
    form = ContactForm()
    context = {"form":form}
    return render(request, "contact.html", context=context)



def dynamic_url(request, id, name):
    print(f"this is the id=")
    return render(request, "dynamic_url.html", context={"id":id, "name":name})

def project(request):
    secret_number = random.randint(1,10)
    context = {"secret_number":secret_number}
    return render(request, "./project/project.html", context)