from django.shortcuts import render

from posts.models import Post, Hashtag


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        context_data = {
            'posts': posts
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
            'post': post
        }

        return render(request, 'posts/detail.html', context=context_data)








