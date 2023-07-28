from django.shortcuts import render
from app.models import Post, Tag


def index(request):
    return render(request, 'app/index.html')


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    tags = Tag.objects.all()

    context = {
        'post': post,
        'tags': tags,
    }
    return render(request, 'app/post.html', context)

