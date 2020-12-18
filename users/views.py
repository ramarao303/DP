from django.shortcuts import render,HttpResponse

# Create your views here.
def users_home():
    return HttpResponse("users Home Page")