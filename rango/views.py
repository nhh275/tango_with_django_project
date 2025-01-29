from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
    # return HttpResponse("<a href='/rango/about'>Rango says hey there partner!</a>")
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, cnady, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # return HttpResponse("<a href='/rango/index'>Rango says here is the about page.</a>")
    context_dict = {'boldmessage': 'This tutorial has been created by Nelson.'}
    return render(request, 'rango/about.html', context=context_dict)
