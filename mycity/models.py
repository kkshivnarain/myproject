from django.db import models
import random
import string

# Create your models here.

def otp_generator():
    otp=''.join([random.choice(string.digits) for i in range(0, 4)])
    return otp

class OTP(models.Model):
    phone= models.CharField(max_length=10,primary_key=True)
    otp=models.CharField(max_length=4,editable=False)
    verified=models.BooleanField(default=False,editable=False)

    def __unicode__(self):
        return self.phone

    def save(self, *args, **kwargs):
        self.otp=otp_generator()
        super(OTP, self).save(*args, **kwargs)

class MyCity(models.Model):
    category=models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude=models.DecimalField(max_digits=10, decimal_places=7)
    timestamp=models.DecimalField(max_digits=13,decimal_places=3)
    city=models.CharField(max_length=50)

    def __unicode__(self):
        return self.city+"-"+self.category


class CityList(models.Model):
    city=models.CharField(max_length=50)
    ne_latitude = models.DecimalField(max_digits=10, decimal_places=7)
    ne_longitude = models.DecimalField(max_digits=10, decimal_places=7)
    sw_latitude = models.DecimalField(max_digits=10, decimal_places=7)
    sw_longitude = models.DecimalField(max_digits=10, decimal_places=7)



class IssueList(models.Model):
    category=models.CharField(max_length=20)
    category_desc=models.CharField(max_length=50)

#https://maps.googleapis.com/maps/api/geocode/json?address=Panchkula
