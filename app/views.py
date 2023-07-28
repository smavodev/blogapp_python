from django.shortcuts import render
from app.models import Post


def index(request):
    return render(request, 'app/index.html')


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'app/post.html')

