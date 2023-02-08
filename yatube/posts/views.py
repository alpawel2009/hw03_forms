from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from .models import Post, Group, User
from .forms import PostForm

POSTS_AMOUNT = 10


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, POSTS_AMOUNT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }

    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.all()
    paginator = Paginator(post_list, POSTS_AMOUNT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    user = User.objects.get(username=username)
    user_posts = Post.objects.filter(author=user)
    user_posts_count = len(user_posts)
    paginator = Paginator(user_posts, POSTS_AMOUNT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'user': user,
        'page_obj': page_obj,
        'user_posts_count': user_posts_count,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    user = post.author
    user_posts_count = len(Post.objects.filter(author=user))
    context = {
        'post': post,
        'user': user,
        'user_posts_count': user_posts_count,
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    form = PostForm(request.POST)
    groups = Group.objects.all()
    context = {
        'groups': groups,
        'form': form,
    }
    if form.is_valid():
        form.instance.author = request.user
        form.save()
        return redirect('posts:profile', request.user)
    return render(request, 'posts/create_post.html', context)


@login_required
def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user != post.author:
        return redirect('posts:post_detail', post_id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect('posts:profile', request.user)
    form = PostForm(instance=post)
    context = {
         'form': form,
         'post': post,
         'is_edit': True,
    }
    return render(request, 'posts/create_post.html', context)