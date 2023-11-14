from django.db import models
from Adminapp.models import *
from django.db.models.deletion import CASCADE
# Create your models here.
class Contactuser(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Customerlogin(models.Model):
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50 ,default='null')
    

    def __str__(self):
        return self.name
    

class Customerregister(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user_id=models.ForeignKey(Customerregister,on_delete=models.CASCADE,null=True,blank=False)
    productid=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=False)
    status=models.IntegerField(default=0)
    total=models.IntegerField()
    quantity=models.IntegerField()

    

class Bookinguser(models.Model):
    user_id=models.ForeignKey(Customerregister,on_delete=models.CASCADE,null=True,blank=False)
    cartid=models.ForeignKey(Cart,on_delete=models.CASCADE,null=True,blank=False)
    name=models.CharField(max_length=50)
    phonenumber=models.IntegerField()
    address=models.CharField(max_length=255)
    zipcode=models.IntegerField()

    def __str__(self):
        return self.name
    

