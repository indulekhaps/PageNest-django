from django.db import models

# Create your models here.
class Category(models.Model):
    Category_name=models.CharField(max_length=40,null=True,blank=True)
    Description=models.TextField(null=True,blank=True)
    Cover_img=models.ImageField(upload_to="category",null=True,blank=True)
class Bookdb(models.Model):
    Book_name=models.CharField(max_length=40,null=True,blank=True)
    Author=models.CharField(max_length=40,null=True,blank=True)
    Category_name=models.CharField(max_length=40,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Publisher=models.CharField(max_length=40,null=True,blank=True)
    Description = models.TextField(null=True, blank=True)
    Cover_pic=models.ImageField(upload_to="books",null=True,blank=True)