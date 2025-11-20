from django.db import models

class Category(models.Model):
    name = models.CharField(max_length= 200)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

