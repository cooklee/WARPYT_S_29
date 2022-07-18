from random import randint

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return HttpResponse('Hello World')


def index2(request):
    http_response = render(request, 'index.html')
    return http_response


def przedstaw(request):
    x = ['slawek', 'Kasia', 'paweł', 'Gosia', 'Ptys']
    imie = x[randint(0, len(x) - 1)]
    return render(request, 'p.html', {'jajko': imie} )
