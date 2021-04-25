from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

def iichome(request):
    return render(request, 'iic/home.html')

def error_view(request):
    return render(request, 'iic/home.html')
