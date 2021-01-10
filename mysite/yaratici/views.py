from .models import BlogPost
from django.shortcuts import get_object_or_404, render

# Create your views here.
def landing_page(request):
    return render(request,'yaratici/landing.html')
def home(request):
    posts = BlogPost.objects.order_by('-create_date')[:3]
    print(posts)
    kimim = BlogPost.objects.get(slug__iexact="ben-kimim")
    return render(request,'yaratici/home.html',{'kimim':kimim,'posts':posts})


def posts(request):
    posts = BlogPost.objects.all().exclude(id=1).order_by('-create_date')
    return render(request,'yaratici/posts.html',{'posts':posts})


def show_post(request,slug):
    posts = BlogPost.objects.all().exclude(id=1).order_by('-create_date')[:10]
    post = get_object_or_404(BlogPost,slug=slug)
    return render(request,'yaratici/post.html',{'post':post, 'posts':posts})