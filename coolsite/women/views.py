from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

# Create your views here.
def index(request): #HttpRequests
    return HttpResponse("Страница приложения women.")

def categories(request, catid):
    if (request.POST):
        print(request.POST)

    return HttpResponse(f"<h1>Статья по категориям</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)
    
    return HttpResponse(f"<h1>Арки по годами</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена.</h1>")