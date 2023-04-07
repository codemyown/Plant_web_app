from django.shortcuts import render
from django.http import HttpResponse
from .models.contact import Contact
from .models.product import Product

# Create your views here.




def index(request):
    products = Product.get_all_products()
    
    
    
    
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']
        contact = Contact(name = name,email = email,number = number,
                          message = message)
        contact.save()
        

    return  render(request,"index.html",{'myproduct':products})