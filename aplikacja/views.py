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


def przedsawsie(request, imie, nazwisko):
    return render(request, 'p4.html', {'imie':imie, 'nazwisko':nazwisko})

def tabliczka(request, a, b):
    s = ""
    for x in range(1, a+1):
        for y in range(1, b+1):
            s+= f"{x*y} "
        s+= "<br>"
    return HttpResponse(s)

def tabliczka_render(request, a, b):
    wynik = []
    for x in range(1, a+1):
        maly_wynik = []
        for y in range(1, b+1):
            maly_wynik.append(x*y)
        wynik.append(maly_wynik)
    return render(request, 'tabliczka.html', {'tab':wynik})