from django.db import models
from django.utils import timezone


# Create your models here.
class Customer(models.Model):
    email = models.TextField(null=False, default='')
    password = models.TextField(null=False, default='')
    name = models.TextField(null=False, default='')


class Cart(models.Model):
    count = models.IntegerField(default=1)
    added = models.DateTimeField(default=timezone.now)
    customer_id = models.IntegerField(null=False)
    product_id = models.IntegerField(null=False)
