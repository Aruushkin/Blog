from django.contrib import admin
from django.urls import path

from posts.views import main_view, posts_view, hashtags_view
from products.views import products_view, categories_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('posts/', posts_view),
    path('products/', products_view),
    path('hashtags/', hashtags_view),
    path('categpries,', categories_view),
]
