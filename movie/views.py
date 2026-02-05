from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("<h1>Welcome to Home Page</h1>")
    return render(request, 'home.html', {'name': 'Juan Escobar'})

def about(request):
    #return HttpResponse("Welcome to About Page")
    return render(request, 'about.html', {'name': 'Juan Escobar'})