from django.contrib import admin
from .models.contact import Contact
from .models.product import Product
# Register your models here.

admin.site.register(Contact)
admin.site.register(Product)
