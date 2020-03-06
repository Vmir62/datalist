from django.db import models

# Create your models here.

class Customers(models.Model):
    CUSTOMERS=(('0','Recomendation'),
          ('1','Internet'),('2','By Chance'))
    fio= models.CharField(max_length=96,blank=False,unique=False, null=True)
    fio_bolhoy = models.CharField(max_length=96, blank=False, unique=False, null=True)
    blacklist=models.BooleanField(default=False)
    opisanie_bolnoy=models.TextField(max_length=4096,null=True,blank=False)
    photo=models.ImageField(blank=True,upload_to='images/customers',height_field=300)
    vozrast=models.IntegerField(default=16,)
    nachato=models.DateField(blank=True,null=True,default=None)
    zaversheno = models.DateField(blank=True, null=True, default=None)
    diagnoz= models.TextField(max_length=1024,blank=True)
    dop_document1=models.FileField(upload_to='cover/customers/docs',blank=True)
    dop_document2 = models.FileField(upload_to='cover/customers/docs', blank=True)
    dop_document3 = models.FileField(upload_to='cover/customers/docs', blank=True)
    price=models.DecimalField(default=0,max_digits=8,decimal_places=2)
    telefon1= models.CharField(max_length=48,null=True,unique=True)
    telefon2 = models.CharField(max_length=48, null=True, unique=True)
    customer_adress=models.CharField(max_length=96,null=True)
    bolnoy_adress = models.CharField(max_length=96, null=True)
    rezume=models.TextField(max_length=1024,blank=True)

