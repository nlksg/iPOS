from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.accounts_dashboard, name='dashboard'),
    path('chart/', views.chart_of_accounts, name='chart'),
    path('transactions/', views.transaction_list, name='transactions'),
]