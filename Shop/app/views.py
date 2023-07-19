from django.shortcuts import render
from django.http import HttpResponse

from .models import Cart


# Create your views here.
def home(req):
    return HttpResponse(render(req, 'home.html'))


def cart(req):
    return HttpResponse(render(req, 'cart.html', {
        'data': Cart.objects.all()
    }))


def customer(req):
    return HttpResponse(render(req, 'customer.html'))
