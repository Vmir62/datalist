from django.db import models

# Create your models here.

class Customers(models.Model):
    CUSTOMERS=(('0','Recomendation'),
          ('1','Internet'),('2','By Chance'))
    title= models.CharField(max_length=28,blank=False,unique=True,choices=CUSTOMERS)
    blacklist=models.BooleanField(default=False)
    authentic=models.CharField(max_length=192,null=True,blank=False)
    photo=models.ImageField(blank=True,upload_to='images/Customers',height_field=300)
    age=models.IntegerField(default=16,)
    angaged=models.DateField(blank=True,null=True,default=None)
    rezume=models.TextField(max_length=1024,blank=True)
    cover=models.FileField(upload_to='cover/Customers',blank=True)
    price=models.DecimalField(default=0,max_digits=8,decimal_places=2)
    customer=models.CharField(max_length=48,null=True,unique=True)
    customer_adress=models.CharField(max_length=96,null=True)
    customer_rezume=models.TextField(max_length=1024,blank=True)
    published=models.DateField(auto_now_add=True,blank=True,null=True)
