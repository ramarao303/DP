from django.shortcuts import render,HttpResponse

# Create your views here.
def portfolio_home(request):
    return HttpResponse("portfolio Home Page")