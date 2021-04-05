from django.shortcuts import render, redirect

def index(request):
    if 'counter' in request.session:
        return redirect("/")
    else:
        request.session['counter'] = 0
    return render(request, "index.html")

def destroy(request):
    del request.session['counter']
    return redirect("/")