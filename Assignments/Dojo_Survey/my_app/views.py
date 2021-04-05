from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "index.html")

def create_user(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    # name_from_form = request.POST['name']
    # location_from_form = request.POST['location']
    # language_from_form = request.POST['language']
    # comment_from_form = request.POST['comment']
    # context = {
    # 	# "name_on_template" : name_from_form,
    #     # "location_on_template" : location_from_form,
    #     # "language_on_template" : language_from_form,
    #     # "comment_on_template" : comment_from_form,
    # }
    return redirect("/result")

def result(request):
    return render(request,"success.html")
    # print(request.POST)