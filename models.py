from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default="default text")
    price = models.FloatField(default="0.0")
    categories_id = models.IntegerField(default="0")
    img = models.ImageField


class Categories_Manager(models.Manager):
    def create_category(self, title):
        category = self.create(title=title)
        #return category


class Categories(models.Model):
    title = models.CharField(max_length=200)
    objects = Categories_Manager()

Categories.objects.create_category("Soft toys")

