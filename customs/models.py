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
    vozrast=models.IntegerField(default=1)
    nachato=models.DateField(blank=True,null=True,default=None)
    zaversheno = models.DateField(blank=True, null=True, default=None)
    diagnoz= models.TextField(max_length=1024,blank=True)
    dop_document1=models.FileField(upload_to='cover/customers/docs', blank=True)
    dop_document2 = models.FileField(upload_to='cover/customers/docs', blank=True)
    dop_document3 = models.FileField(upload_to='cover/customers/docs', blank=True)
    predoplata = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    price=models.DecimalField(default=0,max_digits=8,decimal_places=2)
    telefon1= models.CharField(max_length=48,null=True,unique=True)
    telefon2 = models.CharField(max_length=48, null=True, unique=False)
    customer_adress=models.CharField(max_length=182,null=True)
    bolnoy_adress = models.CharField(max_length=182, null=True)
    rezume=models.TextField(max_length=1024,blank=True)

    def __str__(self):
        return self.fio



class Sidelki(models.Model):
    fio = models.CharField(max_length=96, blank=False, unique=False, null=True)
    strana = models.CharField(max_length=96, blank=False, unique=False, null=True)
    passport= models.CharField(max_length=192, blank=False, unique=False, null=True)
    vozrast = models.IntegerField(default=1950,)
    medic = models.BooleanField(default=False)
    blacklist = models.BooleanField(default=False)
    photo1 = models.ImageField(blank=True, upload_to='images/sidelki', height_field=300)
    photo2 = models.ImageField(blank=True, upload_to='images/sidelki', height_field=600)
    opisanie = models.TextField(max_length=4096, null=True, blank=False)
    v_bolnitse = models.BooleanField(default=False)
    prihodiashaya = models.BooleanField(default=False)
    prozhivaet = models.BooleanField(default=False)
    ozhidaet = models.BooleanField(default=False)
    telefon1 = models.CharField(max_length=48, null=True, unique=True)
    telefon2 = models.CharField(max_length=48, null=True, unique=False)
    adres_registr = models.CharField(max_length=96, null=True)
    adres_proziv = models.CharField(max_length=96, null=True)
    document1recomend = models.FileField(upload_to='cover/sidelki/docs', blank=True)
    document2recomend = models.FileField(upload_to='cover/sidelki/docs', blank=True)
    document1passport = models.FileField(upload_to='cover/sidelki/docs', blank=True)
    document2passport = models.FileField(upload_to='cover/sidelki/docs', blank=True)
    document4passport= models.FileField(upload_to='cover/sidelki/docs', blank=True)
    document3passport = models.FileField(upload_to='cover/sidelki/docs', blank=True)
    document1anketa = models.FileField(upload_to='cover/sidelki/docs', blank=True)
    document2anketa = models.FileField(upload_to='cover/sidelki/docs', blank=True)
    document3anketa = models.FileField(upload_to='cover/sidelki/docs', blank=True)
    list_ozidanie = models.TextField(max_length=1024, blank=True)
    
    
    def __str__(self):
        return self.fio
