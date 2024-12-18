from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)





class Product(models.Model):
    name = models.CharField(max_length=150, default=0)
    description = models.TextField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    create_date = models.DateTimeField(auto_now_add=True)
    write_time = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    image = models.ImageField(upload_to='products/', default='default.jpg')