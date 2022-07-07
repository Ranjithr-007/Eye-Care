from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings



def homepage(request):
    return render(request, 'index.html')