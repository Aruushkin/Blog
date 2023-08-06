from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from Blog import settings
from products import views

from users import views as users_views
from posts.views import main_view, posts_view, hashtags_view, post_detail_view, create_post_view
from products.views import categories_view, product_detail_view, add_review_view, create_category_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='home'),

    path('posts/', posts_view, name='posts_view'),
    path('posts/<int:id>/', post_detail_view),
    path('posts/create/', create_post_view),

    path('products/', views.products_view, name='products_view'),
    path('products/<int:product_id>/', product_detail_view, name='product_detail'),
    path('products/create/', views.create_product_view, name='create_product'),

    path('categories/', categories_view, name='categories_view'),
    path('categories/create/', create_category_view),

    path('hashtags/', hashtags_view),
    path('categories/', categories_view),
    path('product/<int:product_id>/add_review/', views.add_review_view, name='add_review'),

    path('users/register/', users_views.register_view),
    path('users/login/', users_views.login_view),
    path('users/logout/', users_views.logout_view),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
