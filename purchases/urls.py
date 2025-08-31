from django.urls import path
from . import views

app_name = 'purchases'

urlpatterns = [
    path('', views.purchase_list, name='list'),
    path('new/', views.new_purchase, name='new'),
    path('<int:pk>/', views.purchase_detail, name='detail'),
]