from django.db import models

# Create your models here.
CATEGORY_CHOICE=(
    ('BG','bag'),
    ('TT','Table-Top'),
    ('LP','Leather-Pouches'),
    ('WL','Wallet'),
    ('SC','School-Combo'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default="")
    prodapp = models.TextField(default="")
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=2)
    product_image = models.ImageField(upload_to="product")
    def __str__(self):
        return self.title 
