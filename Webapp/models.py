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
