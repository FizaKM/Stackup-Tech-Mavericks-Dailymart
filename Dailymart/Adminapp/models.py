from django.db import models
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    price=models.IntegerField()
    image=models.ImageField(upload_to="sample",default='null.jpg')
    quantity=models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="sample",default='null.jpg')

    def __str__(self):
        return self.name
    


    

    


     

