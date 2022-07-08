from turtle import pos
from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    query = request.GET.get('search_query')
    posts = Post.objects.filter(is_published=True).order_by('-id')
    if query:
        posts = posts.filter(title__icontains=query)
        data = {
        "posts": posts,
        }
        return render(request,'archived.html',data)
    else:
        data = {"posts": posts}
        return render(request,'index.html',data)

def individual_post(request,slug):
    post = Post.objects.get(slug=slug)
    post.views += 1
    post.save()
    data = {
        "posts": post
    }
    return render(request,'individual_post.html',data)

