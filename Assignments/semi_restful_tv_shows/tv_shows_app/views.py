from django.shortcuts import render, redirect
from .models import All_Shows

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
    if request.method == "POST":
        show = All_Shows.objects.get(id=id);
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST["description"]
        show.save()
    return redirect(f"/shows/{id}")

def add(request):
    return render(request, "add_show.html")

def create(request):
    if request.method == "POST":
        print(request.POST)
        show = All_Shows();
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST["description"]
        show.save()
    return redirect(f"/shows/{show.id}")

def delete(request, id):
    show = All_Shows.objects.get(id=id);
    show.delete()
    return redirect("/shows")
