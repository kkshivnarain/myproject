from django.db import models
import random, string, json, urllib, urllib2, datetime
from django.utils import timezone

# Create your models here.

def otp_generator():
    otp=''.join([random.choice(string.digits) for i in range(0, 4)])
    return otp

class OTP(models.Model):
    phone= models.CharField(max_length=10,primary_key=True)
    otp=models.CharField(max_length=4,editable=False)
    first_name=models.CharField(max_length=30, blank=True)
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
    city=models.CharField(max_length=50,blank=True)

    def __unicode__(self):
        return self.city+"-"+self.category

    def save(self, *args, **kwargs):
        if self.pk is None:
            url="http://maps.googleapis.com/maps/api/geocode/json?latlng=" +str(self.latitude)+","+str(self.longitude)
            urlresponse=urllib.urlopen(url)
            googlecity=json.loads(urlresponse.read())
            city=googlecity["results"][0]["address_components"][3]['long_name']
            self.city=city.lower()
            self.latitude=(self.latitude*10000000+int(random.random()*1000))/10000000
            self.longitude=(self.longitude*10000000+int(random.random()*1000))/10000000
        super(MyCity, self).save(*args, **kwargs)

#http://maps.googleapis.com/maps/api/geocode/json?latlng=" +latitude+","+longitude

class CityList(models.Model):
    city=models.CharField(max_length=50)
    ne_latitude = models.DecimalField(max_digits=10, decimal_places=7,blank=True)
    ne_longitude = models.DecimalField(max_digits=10, decimal_places=7,blank=True)
    sw_latitude = models.DecimalField(max_digits=10, decimal_places=7,blank=True)
    sw_longitude = models.DecimalField(max_digits=10, decimal_places=7,blank=True)

    def __unicode__(self):
        return self.city

    def save(self, *args, **kwargs):
        if self.pk is None:
            url="https://maps.googleapis.com/maps/api/geocode/json?address="+self.city
            urlresponse=urllib.urlopen(url) # or use urllib 
            coordinates=json.loads(urlresponse.read())
            self.ne_latitude=coordinates["results"][0]["geometry"]['bounds']['northeast']['lat']
            self.ne_longitude=coordinates["results"][0]["geometry"]['bounds']['northeast']['lng']            
            self.sw_latitude=coordinates["results"][0]["geometry"]['bounds']['southwest']['lat']
            self.sw_longitude=coordinates["results"][0]["geometry"]['bounds']['southwest']['lng']            
        super(CityList, self).save(*args, **kwargs)


class IssueList(models.Model):
    category=models.CharField(max_length=20)
    category_desc=models.CharField(max_length=50)

#https://maps.googleapis.com/maps/api/geocode/json?address=Panchkula

#20160905 Sync with core
class UserCredit(models.Model):#CREATE THIS ALONG WITH USER CREATION IN VIEW
    userid=models.CharField(max_length=10)
    credit=models.DecimalField(max_digits=6,decimal_places=2,default=0.0)
    thisweekcredit=models.DecimalField(max_digits=6,decimal_places=2,default=0.0,editable=False)
    thisweekrank=models.DecimalField(max_digits=3,decimal_places=0,default=0,editable=False)
    lastweekcredit=models.DecimalField(max_digits=6,decimal_places=2,default=0.0,editable=False)
    lastweekrank=models.DecimalField(max_digits=3,decimal_places=0,default=0,editable=False)

    def __unicode__(self):
        return self.userid

    def weekscore(self,weeknumber):
        today=timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        weekday=today.weekday()
        from_date=today-datetime.timedelta(days=weeknumber*7)
        to_date=from_date+datetime.timedelta(days=7)
        try:
            weekcredit=UserCreditDetails.objects.filter(userid=self.userid,
                                         created_date__gte=from_date,
                                         created_date__lte=to_date)
            if weeknumber==0: #Current Week
                self.thisweekcredit=len(weekcredit)
            elif weeknumber==1: #Last Week
                self.lastweekcredit=len(weekcredit)
            else:
                pass
        except Exception:
            pass
        

class UserCreditDetails(models.Model):
    userid=models.CharField(max_length=10)
    created_date=models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            credit=UserCredit.objects.get(userid=self.userid)
            credit.credit+=1
            credit.save()
        super(UserCreditDetails, self).save(*args, **kwargs)
            
    
from django.db import models
import random, string, json, urllib, urllib2, datetime
from django.utils import timezone

# Create your models here.

def otp_generator():
    otp=''.join([random.choice(string.digits) for i in range(0, 4)])
    return otp

class OTP(models.Model):
    phone= models.CharField(max_length=10,primary_key=True)
    otp=models.CharField(max_length=4,editable=False)
    first_name=models.CharField(max_length=30, blank=True)
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
    city=models.CharField(max_length=50,blank=True)

    def __unicode__(self):
        return self.city+"-"+self.category

    def save(self, *args, **kwargs):
        if self.pk is None:
            url="http://maps.googleapis.com/maps/api/geocode/json?latlng=" +str(self.latitude)+","+str(self.longitude)
            urlresponse=urllib.urlopen(url)
            googlecity=json.loads(urlresponse.read())
            city=googlecity["results"][0]["address_components"][3]['long_name']
            self.city=city.lower()
            self.latitude=(self.latitude*10000000+int(random.random()*1000))/10000000
            self.longitude=(self.longitude*10000000+int(random.random()*1000))/10000000
        super(MyCity, self).save(*args, **kwargs)

#http://maps.googleapis.com/maps/api/geocode/json?latlng=" +latitude+","+longitude

class CityList(models.Model):
    city=models.CharField(max_length=50)
    ne_latitude = models.DecimalField(max_digits=10, decimal_places=7,blank=True)
    ne_longitude = models.DecimalField(max_digits=10, decimal_places=7,blank=True)
    sw_latitude = models.DecimalField(max_digits=10, decimal_places=7,blank=True)
    sw_longitude = models.DecimalField(max_digits=10, decimal_places=7,blank=True)

    def __unicode__(self):
        return self.city

    def save(self, *args, **kwargs):
        if self.pk is None:
            url="https://maps.googleapis.com/maps/api/geocode/json?address="+self.city
            urlresponse=urllib.urlopen(url) # or use urllib 
            coordinates=json.loads(urlresponse.read())
            self.ne_latitude=coordinates["results"][0]["geometry"]['bounds']['northeast']['lat']
            self.ne_longitude=coordinates["results"][0]["geometry"]['bounds']['northeast']['lng']            
            self.sw_latitude=coordinates["results"][0]["geometry"]['bounds']['southwest']['lat']
            self.sw_longitude=coordinates["results"][0]["geometry"]['bounds']['southwest']['lng']            
        super(CityList, self).save(*args, **kwargs)


class IssueList(models.Model):
    category=models.CharField(max_length=20)
    category_desc=models.CharField(max_length=50)

#https://maps.googleapis.com/maps/api/geocode/json?address=Panchkula

#20160905 Sync with core
class UserCredit(models.Model):#CREATE THIS ALONG WITH USER CREATION IN VIEW
    userid=models.CharField(max_length=10)
    credit=models.DecimalField(max_digits=6,decimal_places=2,default=0.0)
    thisweekcredit=models.DecimalField(max_digits=6,decimal_places=2,default=0.0,editable=False)
    thisweekrank=models.DecimalField(max_digits=3,decimal_places=0,default=0,editable=False)
    lastweekcredit=models.DecimalField(max_digits=6,decimal_places=2,default=0.0,editable=False)
    lastweekrank=models.DecimalField(max_digits=3,decimal_places=0,default=0,editable=False)

    def __unicode__(self):
        return self.userid

    def weekscore(self,weeknumber):
        today=timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        weekday=today.weekday()
        from_date=today-datetime.timedelta(days=weeknumber*7)
        to_date=from_date+datetime.timedelta(days=7)
        try:
            weekcredit=UserCreditDetails.objects.filter(userid=self.userid,
                                         created_date__gte=from_date,
                                         created_date__lte=to_date)
            if weeknumber==0: #Current Week
                self.thisweekcredit=len(weekcredit)
            elif weeknumber==1: #Last Week
                self.lastweekcredit=len(weekcredit)
            else:
                pass
        except Exception:
            pass
        

class UserCreditDetails(models.Model):
    userid=models.CharField(max_length=10)
    created_date=models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            credit=UserCredit.objects.get(userid=self.userid)
            credit.credit+=1
            credit.save()
        super(UserCreditDetails, self).save(*args, **kwargs)
            
    
