from django.shortcuts import render, redirect
from .models import Books, Authors

def index(request):
    context = {
    	"all_books": Books.objects.all(),
        "all_authors": Authors.objects.all(),
    }
    return render(request, "index.html", context)

def add_book(request):
    if request.method == "POST":
        new_book = Books()
        new_book.title = request.POST['book_title']
        new_book.desc = request.POST['book_desc']
        new_book.save()
        return redirect("/")

def view_book(request, id):
    book = Books.objects.get(id=(id))
    context = {
        "book": Books.objects.get(id=(id)),
        "book_authors": book.authors.all(),
        "authors": Authors.objects.all()
    }
    return render(request, "view_book.html", context)

def authors(request):
    context = {
    	"all_books": Books.objects.all(),
        "all_authors": Authors.objects.all(),
    }
    return render(request, "authors.html", context)

def add_author(request, id):
    if request.method == "POST":
        new_author = Authors()
        new_author.first_name = request.POST['author']
        new_author.save()
        return redirect("/book/<int:id>")

def view_author(request, id):
    author = Authors.objects.get(id=(id))
    context = {
        "author": Authors.objects.get(id=(id)),
        "authors_books": author.books.all(),
        "books": Books.objects.all(),
    }
    return render(request, "view_author.html", context)