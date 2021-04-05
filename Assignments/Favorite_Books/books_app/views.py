from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Books
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
    if "user_id" in request.session:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            "user": User.objects.get(id=request.session['user_id']),
            "books": Books.objects.all(),
            "users_who_like": User.objects.get(id=request.session['user_id']).liked_books.all()
        }
        return render(request, "success.html", context)
    else:
        return redirect("/")
    return redirect("/")

def add(request):
    errors = Books.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/success")
    if request.method == "POST":
        # book.users_who_like.add(User.objects.get(id=request.session['user_id'])
        user = User.objects.get(id=request.session['user_id'])
        book = Books.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            uploaded_by=user
        )
        book.users_who_like.add(user)
        book.save()
    return redirect("/success")

def view_edit(request, id):
    book = Books.objects.get(id=id);
    user = User.objects.get(id=request.session['user_id'])
    uploaded_by = book.uploaded_by
    if user == uploaded_by:
        context = {
            "user": User.objects.get(id=request.session['user_id']),
            "books": Books.objects.all(),
            "uploaded_by": book.uploaded_by
        }
        return redirect(f"/books/{book.id}/edit")
    else:
        return redirect(f"/books/{book.id}/view")

def edit(request, id):
    book = Books.objects.get(id = id)
    user = User.objects.get(id=request.session['user_id'])
    context = {
            "user": User.objects.get(id=request.session['user_id']),
            "book": Books.objects.get(id = id),
            "uploaded_by": Books.objects.first().uploaded_by,
            "users_who_like": book.users_who_like.all()
        }
    return render(request, "edit.html", context)

def view(request, id):
    book = Books.objects.get(id = id)
    user = User.objects.get(id=request.session['user_id'])
    context = {
            "book": book,
            "user": User.objects.get(id=request.session['user_id']),
            "books": Books.objects.get(id = id),
            "users_who_like": book.users_who_like.all()
        }
    return render(request, "view.html", context)

def favorite(request, id):
    user = User.objects.get(id=request.session['user_id'])
    book = Books.objects.get(id = id)
    user.liked_books.add(book)
    user.save()
    return redirect("/success")

def unfavorite(request, id):
    user = User.objects.get(id=request.session['user_id'])
    book = Books.objects.get(id = id)
    user.liked_books.remove(book)
    user.save()
    return redirect(f"/books/{book.id}/edit")

def favorite_other(request, id):
    user = User.objects.get(id=request.session['user_id'])
    book = Books.objects.get(id = id)
    user.liked_books.add(book)
    user.save()
    return redirect(f"/books/{book.id}/view")

def update(request, id):
    book = Books.objects.get(id = id)
    if "update" in request.POST:
        errors = Books.objects.book_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            temp_book = Books()
            temp_book.id = book.id
            temp_book.title = request.POST['title']
            temp_book.description = request.POST['description']
            context = {
                    "user": User.objects.get(id=request.session['user_id']),
                    "book": temp_book,
                    "uploaded_by": Books.objects.first().uploaded_by,
                    "users_who_like": book.users_who_like.all()
                }
            return render(request, "edit.html", context)
        else:
            book.title = request.POST["title"]
            book.description = request.POST["description"]
            book.save()
            return redirect(f"/books/{book.id}/edit")
    elif "delete" in request.POST:
        book.delete()
        return redirect("/success")

