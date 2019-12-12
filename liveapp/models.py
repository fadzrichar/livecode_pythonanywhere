import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    image_path = models.CharField(max_length=255, default = "", blank = True)
    product_name = models.CharField(max_length=255, default = "", blank = True)
    product_price = models.CharField(max_length=30, default = "", blank = True)
    product_desc = models.TextField(max_length=2000, default = None, blank = True)

    def __str__(self):
        return self.product_name