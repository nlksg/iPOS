from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    path('', views.sales_list, name='list'),
    path('new/', views.new_sale, name='new'),
    path('<int:pk>/', views.sale_detail, name='detail'),
]