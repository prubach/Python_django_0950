from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, Group

# Create your views here.
from rest_framework import viewsets

from .models import Customer, Account
from .serializers import CustomerSerializer, AccountSerializer, UserSerializer, GroupSerializer

def index(request):
    return HttpResponse('Welcome to Bank Application!')


def hello(request):
    msg = 'Hello Text from a template'
    return render(request, 'test.html', {'hello_text': msg})


def show_cust(request, cust_id):
    customer = get_object_or_404(Customer, pk=cust_id)
    return render(request, 'cust.html', {'customer': customer})


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
