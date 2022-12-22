from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)
    slug = models.TextField(unique=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category =models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.TextField(unique=True)

    def __str__(self):
        return self.name

class Slider(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media')
    rank= models.IntegerField(null=True)
    url=models.URLField(max_length=500)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name


class Ad(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media')
    rank= models.IntegerField(null=True)
    slug = models.TextField(unique=True)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media')
    description=models.TextField(blank=True)
    slug = models.TextField(unique=True)


    def  __str__(self):

        return self.name


STOCK = (('In stock','In stock'),('Out of stock','Out of stock'))
LABELS = (('hot','hot'),('new','new'),('sale','sale'),('','default'))
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    discounted_price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    specification = models.TextField(blank=True)
    slug = models.TextField(unique=True)
    stock = models.CharField(max_length=100,choices=STOCK)
    labels = models.CharField(max_length=100,choices=LABELS,blank=True)









    def __str__(self):
        return self.name
