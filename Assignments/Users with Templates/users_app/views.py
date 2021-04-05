from django.shortcuts import render, redirect
from .models import Users

def index(request):
    context = {
    	"all_users": Users.objects.all()
    }
    return render(request, "index.html", context)

def process(request):
    firstName = request.POST['first_name']
    lastName = request.POST['last_name']
    email_address = request.POST["email_address"]
    age = request.POST["age"]
    Users.objects.create(first_name=firstName, last_name=lastName, email_address=email_address, age=age)
    return redirect("/")