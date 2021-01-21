from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Welcome to Bank Application!')


def hello(request):
    msg = 'Hello Text from a template'
    return render(request, 'test.html', {'hello_text': msg})