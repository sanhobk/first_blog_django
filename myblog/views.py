from django.shortcuts import render
from django.http import HttpResponse


def index(request):
   return render(request, 'pages/home.html')


def information(request):
   return render(request, 'pages/information.html')


def post(request):
   return render(request, 'pages/post.html')


def contact(request):
   return render(request, 'pages/contact.html')