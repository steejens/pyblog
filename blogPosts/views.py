from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPosts


# Create your views here.

def index(request):
    posts = BlogPosts.objects.all()
    return render(request, 'blogPosts/index.html', {'posts': posts} )
