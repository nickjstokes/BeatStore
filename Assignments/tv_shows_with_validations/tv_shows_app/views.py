from django.shortcuts import render, redirect
from .models import All_Shows
from django.contrib import messages

def redirect_home(request):
    return redirect("/shows")

def index(request):
    context = {
        "all_shows": All_Shows.objects.all()
    }
    return render(request, "index.html", context)

def read_one(request, id):
    context = {
        "show": All_Shows.objects.get(id=id)
    }
    return render(request, "read_one.html", context)

def edit(request, id):
    context = {
        "show": All_Shows.objects.get(id=id)
    }
    return render(request, "edit.html", context)

def update(request, id):
    errors = All_Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{id}/edit")
    else:
    # if request.method == "POST":
        show = All_Shows.objects.get(id=id);
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST["description"]
        show.save()
        messages.success(request, "Show successfully updated")
    return redirect(f"/shows/{id}")

def add(request):
    return render(request, "add_show.html")

def create(request):
    errors = All_Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # return redirect("/shows/new")
        context = {
            "title" : request.POST["title"],
            "network" : request.POST["network"],
            "description": request.POST["description"],
            "release_date": request.POST["release_date"]
        }
        return render(request, "add_show.html", context)
    else:
        # if request.method == "POST":
        show = All_Shows.objects.create(title=request.POST["title"],
        network=request.POST["network"],
        description=request.POST["description"],
        release_date=request.POST["release_date"]);
        messages.success(request, "Show successfully created")
    return redirect(f"/shows/{show.id}")

def delete(request, id):
    show = All_Shows.objects.get(id=id);
    show.delete()
    return redirect("/shows")
