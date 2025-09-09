from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')
    #return HTTP Response

def contato(request):
    return HttpResponse('CONTATO')
    #return HTTP Response

def sobre(request):
    return HttpResponse('SOBRE')
    #return HTTP Response

# Create your views here.
