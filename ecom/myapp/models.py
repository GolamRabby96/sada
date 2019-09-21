from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import math
# Create your models here.

class Category(models.Model):
    cat_name=models.CharField(max_length=255)

    def __str__(self):
        return self.cat_name

class SubCategory(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    cat_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_cat = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    books_name = models.CharField(max_length=255)
    prince = models.FloatField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    image_one = models.ImageField(upload_to='media/profile_pics')
    description_one = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.books_name
