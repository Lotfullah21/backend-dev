from django.shortcuts import render, redirect
from home.forms import ContactForm
from home.models import ContactModel, Product
from django.contrib import messages
import random
# Create your views here.

def index(request):  
    courses = ["ai","js","dl","css","html"]
    age =0
    num = random.randint(10, 1000)
    return render(request,"index.html", context={"random_number":num, "courses":courses, "age":age})

def about(request):
    return render(request, "about.html")

# Validation function
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Product  # Make sure to import your Product model

# Validation function
def isEmptyValue(value):
    return value is None or value == ""

def request_product(request):
    if request.method == "POST":
        product_name = request.POST.get("name")
        remarks = request.POST.get("remarks")
        quantity = request.POST.get("quantity")
        file = request.FILES.get("file")  # Use .get() to avoid KeyError if file is not provided
        
        # Validation
        if isEmptyValue(product_name):
            messages.warning(request, "Product name cannot be null")
            return redirect("/request-product/")
        
        if isEmptyValue(remarks):
            messages.warning(request, "Remarks cannot be null")
            return redirect("/request-product/")
        
        if isEmptyValue(quantity):
            messages.warning(request, "Quantity cannot be null")
            return redirect("/request-product/")
        
        try:
            quantity = int(quantity)
        except ValueError:
            messages.warning(request, "Quantity must be a number")
            return redirect("/request-product/")

        if quantity > 12:
            messages.warning(request, "Product quantity cannot be more than 12")
            return redirect("/request-product/")
        
        if file and not file.name.endswith(".pdf"):
            messages.warning(request, "files can be only pdfs")
            return redirect("/request-product/")
        
        # If all validations pass, create an instance and save it to database.
        product = Product(product_name=product_name, description=remarks, quantity=quantity)
        product.save()

        messages.success(request, "Product submitted successfully!")
        return redirect("/request-product/")
    
    return render(request, "request_product.html")  # Ensure to render the form if GET request


def contact(request):
    if request.method=="POST":
        # get the info from posted request
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
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