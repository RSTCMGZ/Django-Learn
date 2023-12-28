from django.http.response import HttpResponse
from django.shortcuts import render


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
            'title':'Python Kursu',
            'image': '2.jpg',
            'is_active': True,
            'is_home': True,
            'description': 'harika bir kurs',
        },
        {
            'id': 3,
            'title':'Django geliştirme',
            'image': '3.jpg',
            'is_active': False,
            'is_home': True,
            'description': 'harika bir kurs',
        },
    ]
}


# Create your views here.

def index(request):
    context={
        'blogs':data['blogs']
    }
    return render(request,"blog/index.html",context)


def blogs(request):
    context={
        'blogs':data['blogs']
    }
    return render(request,"blog/blogs.html", context)


def blog_details(request,id):
     return render(request,"blog/blog-details.html", {'id': id})