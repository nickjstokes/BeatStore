from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Jobs
import bcrypt

def index(request):
    return render(request, "index.html")

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        hash1 = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            email=request.POST["email"],
            password=hash1
            )
        request.session["user_id"] = user.id
    return redirect("/success")

def login(request):
    userList = User.objects.filter(email=request.POST['email'])
    if userList:
        user = userList[0]
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
            return redirect('/success')
        else:
            messages.error(request, "Login failed")
    else:
        messages.error(request, "Login failed")
    return redirect("/")

def logout(request):
    request.session.clear()
    return redirect("/")

def success(request):
    if "user_id" in request.session:
        user = User.objects.get(id=request.session['user_id'])
        jobs = Jobs.objects.all()
        context = {
            "user": user,
            "jobs": jobs,
        }
        return render(request, "success.html", context)
    else:
        return redirect("/")

def add_job(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        "user": user,
    }
    return render(request, "add_job.html", context)

def cancel(request):
    return redirect("/success")

def add(request):
    errors = Jobs.objects.job_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/add_job")
    if request.method == "POST":
        user = User.objects.get(id=request.session['user_id'])
        job = Jobs.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            location=request.POST["location"],
            uploaded_by=user
        )
        job.save()
    return redirect("/success")

def remove(request, id):
    job = Jobs.objects.get(id = id)
    job.delete()
    return redirect("/success")

def edit(request, id):
    job = Jobs.objects.get(id = id)
    user = User.objects.get(id=request.session['user_id'])
    context = {
            "user": user,
            "job": job,
        }
    return render(request, "edit.html", context)

def update(request, id):
    job = Jobs.objects.get(id = id)
    errors = Jobs.objects.job_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/edit/{job.id}")
    else:
        job.title = request.POST["title"]
        job.description = request.POST["description"]
        job.location = request.POST["location"]
        job.save()
    return redirect("/success")

def view(request, id):
    job = Jobs.objects.get(id = id)
    user = User.objects.get(id=request.session['user_id'])
    context = {
            "job": job,
            "user": user,
        }
    return render(request, "view.html", context)