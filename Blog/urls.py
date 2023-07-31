from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from Blog import settings
from posts.views import main_view, posts_view, hashtags_view, post_detail_view
from products.views import products_view, categories_view, product_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),

    path('posts/', posts_view),
    path('posts/<int:id>/', post_detail_view),

    path('products/', products_view),
    path('products/<int:id>/', product_detail_view),
    path('hashtags/', hashtags_view),
    path('categories/', categories_view),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
