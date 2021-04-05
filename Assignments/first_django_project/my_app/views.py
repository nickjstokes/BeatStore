# Create your views here.
from django.shortcuts import render, HttpResponse, redirect

def root(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')
    
def show(request, id):
    return HttpResponse(f"placeholder to display blog number: {id}")

def edit(request, num):
    return HttpResponse(f"placeholder to edit blog {num}")

def destroy(request, numba):
    return redirect('/blogs')