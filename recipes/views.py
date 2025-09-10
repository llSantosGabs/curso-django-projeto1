from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html', context ={

        'name' : 'Gabriel Santos',

    })
    #return HTTP Response

def contato(request):
    return render(request, 'me-apague/temp.html')
    #return HTTP Response

def sobre(request):
    return HttpResponse('SOBRE')
    #return HTTP Response

# Create your views here.
