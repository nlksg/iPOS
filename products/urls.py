from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # Product pages
    path('', views.product_list, name='product_list'),
    path('<int:pk>/edit/', views.product_edit, name='product_edit'),

    # Media manager
    path('media/', views.media_manager, name='media_manager'),
    path('media/delete/', views.delete_media, name='delete_media'),
    path('media/grid/', views.media_grid, name='media_grid'),
    path('media/upload/', views.upload_media, name='upload_media'),
]