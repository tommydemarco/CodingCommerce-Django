from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category

class Tag(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="azienda/products")
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)
    price = models.FloatField(null=True, blank=True)
    home_page = models.BooleanField(default=False)
    on_sale = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    bio = models.TextField()
    fb_link = models.URLField(max_length=200, null=True, blank=True)
    ig_link = models.URLField(max_length=200, null=True, blank=True)
    tw_link = models.URLField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="azienda/employees")

    def __str__(self):
        return self.name