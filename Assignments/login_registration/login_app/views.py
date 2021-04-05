from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
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
    # get user from database, if list is empty you know this user doesn't currently exist
    userList = User.objects.filter(email=request.POST['email'])
    if userList:
        user = userList[0]

        #                password input from form            hashed pw from database
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        # if we get True after checking the password, we may put the user id in session
            request.session['user_id'] = user.id
        # never render on a post, always redirect!
            return redirect('/success')
        else:
            messages.error(request, "Login failed")
    else:
        messages.error(request, "Login failed")

    return redirect("/")

def logout(request):
    request.session.clear()
    return redirect("/")

# check to see if user is in session, use this to grant access to /success
def success(request):
    try:
        if "user_id" in request.session:
            context = {
                "user": User.objects.get(id=request.session['user_id'])
            }
            return render(request, "success.html", context)
        else:
            return redirect("/")
    except:
        return redirect("/")