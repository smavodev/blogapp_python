from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import render, redirect, get_object_or_404
from app.models import Post, Tag, Comments, Profile, WebsiteMeta
from app.forms import CommentForm, SubscribeForm, NewUserForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login


def index(request):
    posts = Post.objects.all()
    top_posts = Post.objects.all().order_by('-view_count')[0:3]
    recent_posts = Post.objects.all().order_by('-created_date')[0:3]
    featured_blog = Post.objects.filter(is_featured=True)
    subscribe_form = SubscribeForm()
    subscribe_successful = None

    if WebsiteMeta.objects.all().exists():
        website_info = WebsiteMeta.objects.all()[0]

    if featured_blog:
        featured_blog = featured_blog[0]

    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            request.session['subscribed'] = True
            subscribe_successful = 'Subscribed Successfully'
            subscribe_form = SubscribeForm()

    context = {
        'posts': posts,
        'top_posts': top_posts,
        'website_info': website_info,
        'recent_posts': recent_posts,
        'subscribe_form': subscribe_form,
        'subscribe_successful': subscribe_successful,
        'featured_blog': featured_blog,
    }
    return render(request, 'app/index.html', context)


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comments.objects.filter(post=post, parent=None)
    form = CommentForm()

    # Bookmark logic
    bookmarked = False
    if post.bookmarks.filter(id=request.user.id).exists():
        bookmarked = True
    is_bookmarked = bookmarked

    # Liked logic
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True
    number_of_likes = post.number_of_likes()
    post_is_liked = liked

    if request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid:
            parent_obj = None
            if request.POST.get('parent'):
                # save reply
                parent = request.POST.get('parent')
                parent_obj = Comments.objects.get(id=parent)

                if parent_obj:
                    comment_reply = comment_form.save(commit=False)
                    comment_reply.parent = parent_obj
                    comment_reply.post = post
                    comment_reply.save()
                    return HttpResponseRedirect(reverse('post_page', kwargs={'slug': slug}))
            else:
                comment = comment_form.save(commit=False)
                postid = request.POST.get('post_id')
                post = Post.objects.get(id=postid)
                comment.post = post
                comment.save()
                return HttpResponseRedirect(reverse('post_page', kwargs={'slug': slug}))

    if post.view_count is None:
        post.view_count = 1
    else:
        # post.view_count = post.view_count + 1
        post.view_count += 1
    post.save()

    recent_posts = Post.objects.exclude(id=post.id).order_by('-modified_date')[0:3]
    top_authors = User.objects.annotate(number=Count('post')).order_by('number')[0:3]
    tags = Tag.objects.all()
    related_posts = Post.objects.exclude(id=post.id).filter(author=post.author)[0:3]

    number_of_comments = comments.count()

    context = {
        'post': post,
        'form': form,
        'comments': comments,
        'number_of_comments': number_of_comments,
        'is_bookmarked': is_bookmarked,
        'post_is_liked': post_is_liked,
        'number_of_likes': number_of_likes,
        'tags': tags,
        'recent_posts': recent_posts,
        'top_authors': top_authors,
        'related_posts': related_posts
    }
    return render(request, 'app/post.html', context)


def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)

    top_posts = Post.objects.filter(tags__in=[tag.id]).order_by('-view_count')[0:2]
    recent_posts = Post.objects.filter(tags__in=[tag.id]).order_by('-created_date')[0:2]

    tags = Tag.objects.all()
    context = {
        'tag': tag,
        'top_posts': top_posts,
        'recent_posts': recent_posts,
        'tags': tags
    }
    return render(request, 'app/tag.html', context)


def author_page(request, slug):
    profile = Profile.objects.get(slug=slug)

    top_posts = Post.objects.filter(author=profile.user).order_by('-view_count')[0:2]
    recent_posts = Post.objects.filter(author=profile.user).order_by('-modified_date')[0:2]
    top_authors = User.objects.annotate(number=Count('post')).order_by('number')[0:3]

    context = {
        'profile': profile,
        'top_posts': top_posts,
        'recent_posts': recent_posts,
        'top_authors': top_authors
    }
    return render(request, 'app/author.html', context)


def search_posts(request):

    # paged_posts = Post.objects.all()
    paged_posts = None
    post_count = None
    search_query = ''

    if 'search_query' in request.GET:
        search_query = request.GET['search_query']
        if search_query:
            # posts = Post.objects.order_by(title__icontains=search_query)
            posts = Post.objects.order_by('-created_date').filter(Q(title__icontains=search_query))

            if 'search_query' in request.GET and request.GET['search_query']:
                page = request.GET.get('page')
                search_query = request.GET['search_query']
                paginator = Paginator(posts, 6)
            paged_posts = paginator.get_page(page)
            post_count = posts.count()

        if not search_query:
            posts = ''
            post_count = ''

    context = {
        'posts': paged_posts,
        'product_count': post_count,
        'search_query': search_query
    }
    return render(request, 'app/search.html', context)


def about(request):
    website_info = None

    if WebsiteMeta.objects.all().exists():
        website_info = WebsiteMeta.objects.all()[0]

    context = {
        'website_info': website_info
    }
    return render(request, 'app/about.html', context)


def register_user(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create profile
            profile = Profile()
            profile.user = user
            profile.profile_image = 'images/profile/default.jpg'
            profile.bio = 'Perfil por completar, por favor complete su registro'
            profile.save()

            login(request, user)
            return redirect("/")
    context = {
        'form': form
    }
    return render(request, 'registration/registration.html', context)


def bookmark_post(request, slug):
    print("PRINT", request.POST.get('post_id'))
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.bookmarks.filter(id=request.user.id).exists():
        post.bookmarks.remove(request.user)
    else:
        post.bookmarks.add(request.user)
    return HttpResponseRedirect(reverse('post_page', args=[str(slug)]))


def like_post(request, slug):
    print("PRINT", request.POST.get('post_id'))
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_page', args=[str(slug)]))


def all_posts(request):

    all_posts = Post.objects.all()

    paginator = Paginator(all_posts, 6)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'all_posts': paged_posts
    }
    return render(request, 'app/all_posts.html', context)


def all_bookmarked_posts(request):
    all_bookmarked_posts = Post.objects.filter(bookmarks=request.user)

    paginator = Paginator(all_bookmarked_posts, 6)
    page = request.GET.get('page')
    all_bookmarked_paged_posts = paginator.get_page(page)

    context = {
        'all_bookmarked_posts': all_bookmarked_paged_posts
    }
    return render(request, 'app/all_bookmarked_posts.html', context)


def all_liked_posts(request):
    all_liked_posts = Post.objects.filter(likes=request.user)

    paginator = Paginator(all_liked_posts, 6)
    page = request.GET.get('page')
    all_liked_paged_posts = paginator.get_page(page)

    context = {
        'all_liked_posts': all_liked_paged_posts
    }
    return render(request, 'app/all_liked_posts.html', context)


def top_posts(request):

    top_posts = Post.objects.all().order_by('-view_count')

    paginator = Paginator(top_posts, 9)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'top_posts': paged_posts
    }
    return render(request, 'app/top_posts.html', context)


def recent_posts(request):

    recent_posts = Post.objects.all().order_by('-created_date')

    paginator = Paginator(recent_posts, 9)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'recent_posts': paged_posts
    }
    return render(request, 'app/recent_posts.html', context)
