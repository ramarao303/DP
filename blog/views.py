from django.shortcuts import render,HttpResponse
from . import models
from .models import Post
# Create your views here.
def blog_home(request):
    return render(request,'blog/index.html')
    
def blog_list(request):
    post = Post.objects.all()
    return render(request, "blog/index.html", {'blog_list': post})

def technlogies(request):
    return render(request,'blog/Technlogies.html',context)
posts = [

{
  'author' : 'Loonycorn',
  'title' : 'Blog Post 1',
  'content' : 'First post content',
  'date_posted' : 'October 25, 2019'
},
{
  'author' : 'Test',
  'title' : 'Blog Post 2',
  'content' : 'Second post content',
  'date_posted' : 'October 26, 2019'
}

]


context = {

  'posts' : posts

  }

context = {

  'posts' : posts

  }
def personal(request):
    return render(request,'blog/personal.html')

def public(request):
    return render(request,'blog/public.html')


def blog_post(request,pk):
    post = Post.objects.get(pk=pk)
    return render(request, "blog/blog_post.html", {'post':post})
