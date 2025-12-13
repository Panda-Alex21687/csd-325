from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

def home(request):
     return HttpResponse("Baldree says Hello!")
