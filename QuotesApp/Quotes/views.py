from django.shortcuts import render
from .models import Author,Quote,Tag
from django.http import HttpResponse

def index(request):
    return HttpResponse("Data Uploaded")