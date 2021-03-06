from django.contrib.auth import default_app_config, get_permission_codename
from django.db import models

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_DEFAULT
from django.db.models.fields import NullBooleanField

class Customer(models.Model):
    user = models.OneToOneField(User , null=True , blank=True , on_delete=models.CASCADE)
    name = models.CharField(max_length=200 , null=True)
    email = models.CharField(max_length=60)


    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200 , null=True)
    price = models.FloatField()
    digital = models.BooleanField(null=True , default=False , blank=True)
    image = models.ImageField(null=True , blank=True)

    def __str__(self) -> str:
        return self.name


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.SET_NULL , null=True , blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=True)
    transation_id = models.CharField(max_length=100 , null=True)

    def __str__(self) -> str:
        return str(self.transation_id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_item(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    


    

class OrderItem(models.Model):
    product = models.ForeignKey(Product , on_delete=models.SET_NULL , null=True)
    order = models.ForeignKey(Order , on_delete=models.SET_NULL , null=True)
    quantity = models.IntegerField( default=0 ,null = True , blank = True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity

        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.SET_NULL , null=True)
    order = models.ForeignKey(Order , on_delete=models.SET_NULL , null=True)
    address = models.CharField(max_length=200 , null=False)
    city = models.CharField(max_length=200 , null=False)
    zipcode = models.CharField(max_length=200 , null=False)
    state= models.CharField(max_length=200 , null=False)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.address


        


    
    




