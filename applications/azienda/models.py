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
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)
    home_page = models.BooleanField(default=False)
    on_sale = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    