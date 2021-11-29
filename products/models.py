from django.db import models

class Products(models.Model):
        name=models.CharField(max_length=280)
        price=models.FloatField()
        stock=models.FloatField()
        img_urls=models.CharField(max_length=2083)

class offer(models.Model):
    code =models.CharField(max_length=5)
    description=models.TextField()
    discount=models.FloatField()

