from django.shortcuts import render
from django.http import HttpResponse

# from blog.models import Post
#
# # Create your views here.
#
# class PostListView(ListView):
#     models=Post
#
# class PostDetailView(detal):
#     models=Post


def hello_world(request):
    return HttpResponse("Hello World!")

def start_blog(requrset):
    if requrset.method == 'GET':
        return render(requrset,
                      'myblog.html',
                      {'name' : 'Sam_Name'})