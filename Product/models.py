from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class catagory(models.Model):
    name = models.CharField(max_length=50)

def __str__(self):
    return self.name

class product(models.Model):
    name = models.CharField(max_length=30)
    product_image = models.ImageField(upload_to='Product_image/')
    old_prize = models.PositiveIntegerField()
    new_prize = models.PositiveIntegerField()
    catagory = models.ForeignKey(catagory,on_delete= models.CASCADE)
    quantity = models.IntegerField()
    description = models.TextField(max_length=50)
    
def __str__(self):
    return self.name

    