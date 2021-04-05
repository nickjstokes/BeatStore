from django.shortcuts import render, HttpResponse, redirect
from .models import Ninjas, Dojos

def index(request):
    context = {
    	"all_ninjas": Ninjas.objects.all(),
        "all_dojos": Dojos.objects.all(),
    }
    return render(request, "index.html", context)

def add_dojo(request):
    dojo_name = request.POST['name']
    city = request.POST['city']
    state = request.POST['state']
    Dojos.objects.create(name=dojo_name, city=city, state=state)
    return redirect("/")

def add_ninja(request):
    if request.method == "POST":
        ninja = Ninjas()
        ninja.first_name = request.POST['first_name']
        ninja.last_name = request.POST['last_name']
        ninja.default_dojo = Dojos.objects.get(id=request.POST['default_dojo'])
        ninja.save()
        return redirect("/")
