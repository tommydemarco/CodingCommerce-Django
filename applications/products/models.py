from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=70, default="default product subtile")
    clean_url = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField('Image', default="default-category.jpg", upload_to='categories')

    class Meta:
        verbose_name        = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Product(models.Model):
    name            = models.CharField(max_length=50)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    price           = models.FloatField()
    description     = models.TextField(max_length=500)
    #tags            = models.ManyToManyField(Tag)
    image           = models.ImageField('Image', default="default-product.jpg", upload_to='products')
    link            = models.CharField(max_length=100)
    new             = models.BooleanField(default=False)
    on_sale         = models.BooleanField(default=False)
    hottest_deal    = models.BooleanField(default=False)

    def __str__(self):
        return self.name 