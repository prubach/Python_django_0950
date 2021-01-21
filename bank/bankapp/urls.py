from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello, name='Hello'),
    path('<int:cust_id>/', views.show_cust, name='Customer')
]
