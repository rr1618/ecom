from django.db import models

# Create your models here.


class Products(models.Model):
    product_number = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    product_image = models.FileField(verbose_name="Product image", upload_to='pkart/images',
                                     default="")
    product_description = models.CharField(max_length=400)
    product_price = models.CharField(max_length=10)

    def __str__(self):
            return self.product_name
