from django.shortcuts import render, HttpResponse, redirect
def index(request):
    import random
    answer = random.randint(1, 100)
    request.session['answer'] = answer
    return render(request, "index.html")

def process(request):
    guess = int(request.POST['guess'])
    answer = int(request.session['answer'])
    if guess > answer:
        return redirect('/too_high')
    elif guess < answer:
        return redirect('/too_low')
    elif guess == answer:
        return redirect('/correct')

def too_high(request):
    return render(request, "too_high.html")

def too_low(request):
    return render(request, "too_low.html")

def correct(request):
    answer = request.session['answer']
    return render(request, "correct.html", {'guess' : answer})