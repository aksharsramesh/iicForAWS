# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def allevents_view(request):
    return render(request, 'events/allevents.html')
def allevents20_view(request):
    return render(request, 'events/allevents20.html')
def it2020(request):
        return render(request, 'events/it20events.html')
def innvoc1(request):
        return render(request, 'events/innvoc1.html')


def ipr(request):
    return render(request, 'events/iprevent.html')

def it19(request):
    return render(request, 'events/it19event.html')

def pd(request):
    return render(request, 'events/pdevent.html')

def od(request):
    return render(request, 'events/odevent.html')

def kyp(request):
    return render(request, 'events/kypevent.html')

def ltl(request):
    return render(request, 'events/ltlevent.html')

def ht19(request):
    return render(request, 'events/ht19event.html')
