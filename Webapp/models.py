from django.db import models

# Create your models here.
class contactdb(models.Model):
    Name=models.CharField(max_length=40,null=True,blank=True)
    Email=models.EmailField(null=True,blank=True)
    Subject=models.CharField(max_length=40,null=True,blank=True)
    Message=models.TextField(null=True,blank=True)

class Registerdb(models.Model):
    Username=models.CharField(max_length=40,null=True,blank=True)
    Password=models.CharField(max_length=40,null=True,blank=True)
    Conf_password=models.CharField(max_length=40,null=True,blank=True)
    Email=models.EmailField(null=True,blank=True)

class Cartdb(models.Model):
    Username = models.CharField(max_length=40, null=True, blank=True)
    Book_name = models.CharField(max_length=40, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Total_price= models.IntegerField(null=True, blank=True)
    Book_img = models.ImageField(upload_to="Cart", null=True, blank=True)