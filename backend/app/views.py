from django.shortcuts import render

def home(request) :
  return render(request, "app/home.html")

def login_register(request) :
  return render(request, "app/login.html")