from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50)

    class Meta:
        verbose_name        = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('Name', max_length=50)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name

class Product(models.Model):
    name            = models.CharField(max_length=50)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    price           = models.FloatField()
    description     = models.TextField(max_length=500)
    tags            = models.ManyToManyField(Tag)
    image           = models.ImageField('Image', default="default-product.jpg", upload_to='products')
    link            = models.CharField(max_length=100)
    new             = models.BooleanField(default=False)
    on_sale         = models.BooleanField(default=False)