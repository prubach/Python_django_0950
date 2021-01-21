from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'accounts', views.AccountViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello, name='Hello'),
    path('', include(router.urls)),
    path('<int:cust_id>/', views.show_cust, name='Customer')
]
