from django.shortcuts import render,HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def users_home(request):
    return HttpResponse("users Home Page")

def register(request):
    form = UserCreationForm()
    return render(request,'users/register.html',{'form':form})
