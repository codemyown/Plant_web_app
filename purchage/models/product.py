from django.db import models

class Product(models.Model):
    discount = models.IntegerField(default = 0)
    image = models.ImageField(upload_to = "upload/image")
    product_name = models.CharField(max_length = 30)
    price = models.IntegerField(default = 0)
    original_price = models.IntegerField(default = 0)


    def __str__(self):
        return self.product_name
    
    def get_all_products():
        return Product.objects.all()
    

