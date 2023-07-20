import os

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from .models import Cart

# Create your views here.

# TODO: В home нужно передать:
#  categories - все категории из БД
#  selected_category - id первой категории
#  products - продукты из модели Product по выбранной категории (selected_category)

products = [
    {
        'id': 1,
        'title': 'Notebook Acer Aspire 7 A715-42G-R3EZ',
        'description': 'Description product',
        'price': '1000',
        'category_id': 2,
        'img': '8d261abc4c96bfbde4cb9d117e63ffc8.webp'
    },
    {
        'id': 2,
        'title': 'Notebook Acer Aspire 7 A715-42G-R3EZ',
        'description': 'Description product',
        'price': '1000',
        'category_id': 2,
        'img': '8d261abc4c96bfbde4cb9d117e63ffc8.webp'
    },
    {
        'id': 3,
        'title': 'Notebook Acer Aspire 7 A715-42G-R3EZ',
        'description': 'Description product',
        'price': '1000',
        'category_id': 2,
        'img': '8d261abc4c96bfbde4cb9d117e63ffc8.webp'
    },
    {
        'id': 4,
        'title': 'Notebook Acer Aspire 7 A715-42G-R3EZ',
        'description': 'Description product',
        'price': '1000',
        'category_id': 2,
        'img': '8d261abc4c96bfbde4cb9d117e63ffc8.webp'
    },
    {
        'id': 5,
        'title': 'Notebook Acer Aspire 7 A715-42G-R3EZ',
        'description': 'Description product',
        'price': '1000',
        'category_id': 2,
        'img': '8d261abc4c96bfbde4cb9d117e63ffc8asd.webp'
    },
    {
        'id': 6,
        'title': 'Notebook Acer Aspire 7 A715-42G-R3EZ',
        'description': 'Description product',
        'price': '1000',
        'category_id': 2,
        'img': '8d261abc4c96bfbde4cb9d117e63ffc8.webp'
    },
]


# Checks if there is a product image, if not, replaces it 'no-image.png'
def images_exists(product):
    print(os.path.join(settings.STATICFILES_DIRS[0], 'images',
                       product['img']))
    product['img'] = product['img'] if os.path.exists(os.path.join(settings.STATICFILES_DIRS[0], 'images',
                                                                   product['img'])) else 'no-image.png'
    return product


def home(req):
    return HttpResponse(render(req, 'home.html', {
        'categories': [
            {
                'id': 1,
                'title': 'Computers'
            },
            {
                'id': 2,
                'title': 'Phones'
            },
            {
                'id': 3,
                'title': 'Household appliances'
            },
            {
                'id': 4,
                'title': 'Goods for gamers'
            }
        ],
        'selected_category': 2,
        'products': list(map(images_exists, products)),
        'count_in_cart': Cart.objects.filter(customer_id=1).count()
    }))


def cart(req):
    data = Cart.objects.filter(customer_id=1)
    return HttpResponse(render(req, 'cart.html', {
        'data': data,
        'count_in_cart': len(data)
    }))


def customer(req):
    return HttpResponse(render(req, 'customer.html', {
        'count_in_cart': Cart.objects.filter(customer_id=1).count()
    }))
