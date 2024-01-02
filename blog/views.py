from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog

data = {
    'blogs': [
        {
            'id': 1,
            'title':'Web geliştirme',
            'image': '1.jpg',
            'is_active': True,
            'is_home': False,
            'description': 'harika bir kurs',
        },
        {
            'id': 2,
            'title':'Node Kursu',
            'image': '2.jpg',
            'is_active': True,
            'is_home': True,
            'description': 'Dünyada en çok kullanılan bir dil.',
        },
        {
            'id': 3,
            'title':'Python Kursu',
            'image': '3.jpg',
            'is_active': False,
            'is_home': True,
            'description': 'Kolay öğrenme imkanı sunar.',
        },
    ]
}


# Create your views here.

def index(request):
    context={
        'blogs': Blog.objects.filter(is_active = True, is_home = True)
    }
    return render(request,"blog/index.html",context)


def blogs(request):
    context={
        'blogs': Blog.objects.filter(is_active = True)
    }
    return render(request,"blog/blogs.html", context)


def blog_details(request,slug):

    blog = Blog.objects.get(slug=slug)
    return render(request,"blog/blog-details.html", {'blog': blog})