from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .models import Customer


def index(request):
    return HttpResponse('Welcome to Bank Application!')


def hello(request):
    msg = 'Hello Text from a template'
    return render(request, 'test.html', {'hello_text': msg})


def show_cust(request, cust_id):
    customer = get_object_or_404(Customer, pk=cust_id)
    return render(request, 'cust.html', {'customer': customer})