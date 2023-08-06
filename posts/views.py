from django.db.models import Q
from django.shortcuts import render, redirect

from posts.constants import PAGINATION_LIMIT
from posts.forms import PostForm
from posts.models import Post, Hashtag


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()

        max_page = posts.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        search_text = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if search_text:
            """startswith, endswith, icontains"""
            posts = posts.filter(Q(title__startswith=search_text) |
                                Q(description__icontains=search_text))

        """Pagination"""
        posts = posts[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]
        """3:6"""

        context_data = {
            'posts': posts,
            'user': request.user,
            'pages': range(1, max_page+1)
        }
        return render(request, 'posts/posts.html', context=context_data)


def hashtags_view(request):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()

        context_data = {
            'hashtags': hashtags
        }

        return render(request, 'hashtags/hashtags.html', context=context_data)


def post_detail_view(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)
        context_data = {
            'post': post,
            'user': request.user
        }

        return render(request, 'posts/detail.html', context=context_data)


def create_post_view(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts_view')

    return render(request, 'posts/create_post.html', {'form': form})








