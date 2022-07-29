from email.mime import image
from tabnanny import verbose
from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.
# Home ej
class HomeBG(models.Model):
    name1 = models.CharField('BG name1', max_length=30)
    name2 = models.CharField('BG name2', max_length=30)
    about = models.TextField('BG about')
    img = models.ImageField('BG image', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeBG'
        verbose_name_plural = 'HomeBGS'


class TourIdea(models.Model):
    name = models.CharField('Idea name', max_length=50)
    about = models.TextField('Idea about')
    img = models.ImageField('Idea image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TourIdea'
        verbose_name_plural = 'TourIdeas'

class Mezhet(models.Model):
    name = models.CharField('mezh name', max_length=50)
    about = models.TextField('mezh about')
    img = models.ImageField('mezh image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mezhet'
        verbose_name_plural = 'Mezhets'

class Apranqner(models.Model):
    name = models.CharField('apranq name', max_length=50)
    price = models.IntegerField('apranq price')
    img = models.ImageField('apranq image', upload_to='media')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Apranqer'
        verbose_name_plural = 'Apranqners'

class Amragir(models.Model):
    name = models.CharField('amrqagir name', max_length=50)
    about = models.TextField('amragir about')
    img = models.ImageField('amragir image', upload_to='media')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Amragir'
        verbose_name_plural = 'Amragirs'

class ChampordVayr(models.Model):
    name = models.CharField('vayr name', max_length=50)
    about = models.TextField('vayr about')
    img = models.ImageField('vayr image', upload_to='media')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ChampordVayr'
        verbose_name_plural = 'ChampordVayrs'

class Karciqner(models.Model):
    name1= models.CharField('Karc name1', max_length=50)
    name2 = models.CharField('Karc name2', max_length=40, null=True)
    about = models.TextField('Karc about')
    img = models.ImageField('Karc image', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'Karciqner'
        verbose_name_plural = 'Karciqners'



# Mer Masin
class About(models.Model):
    name1 = models.TextField('About name1')
    name2 = models.TextField('About name2')
    img = models.ImageField('About image',  upload_to='media')
    
    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

# hyuranoc stays
class Staysmin(models.Model):
    name = models.IntegerField('staysmin name', null=True, blank=True)
    name2 = models.IntegerField('staysmin name1', null=True, blank=True)
    name3 = models.IntegerField('staysmin name2', null=True, blank=True)
    name4 = models.IntegerField('staysmin name3', null=True, blank=True)
    name5 = models.IntegerField('staysmin name4', null=True, blank=True)
    
    def __int__(self):
        return self.name

    class Meta:
        verbose_name = 'Staysmin'
        verbose_name_plural = 'Staysmins'


class Staysmax(models.Model):
    name = models.IntegerField('staysx name1')
    name2 = models.IntegerField('staysx name2')
    name3 = models.IntegerField('staysx name3')
    name4 = models.IntegerField('staysx name4')
    name5 = models.IntegerField('staysx name5')
    
    def __int__(self):
        return self.name

    class Meta:
        verbose_name = 'Staysmax'
        verbose_name_plural = 'Staysmaxs'

class PropertyST(models.Model):
    name = models.CharField('property status', max_length=30)
    name2 = models.CharField('property status2', max_length=30)
    name3 = models.CharField('property status3', max_length=30)
    name4 = models.CharField('property status4', max_length=30)
    name5 = models.CharField('property status5', max_length=30)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'PropertyST'
        verbose_name_plural = 'PropertySTs'

class PropertyTyp(models.Model):
    name = models.CharField('property type', max_length=30)
    name2 = models.CharField('property type2', max_length=30)
    name3 = models.CharField('property type3', max_length=30)  
    name4 = models.CharField('property type4', max_length=30)
    name5 = models.CharField('property type5', max_length=30)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'PropertyTyp'
        verbose_name_plural = 'PropertyTyps'

class BHK(models.Model):
    name = models.IntegerField('BHK')
    name2 = models.IntegerField('BHK2')
    name3 = models.IntegerField('BHK3')
    name4 = models.IntegerField('BHK4')
    name5 = models.IntegerField('BHK5') 
    
    
    def __int__(self):
        return self.name

class Meta:
    verbose_name = 'BHK'
    verbose_name_plural = 'BHKs'

class Aminit(models.Model):
    name = models.CharField('aminites name', max_length=30)
    name2 = models.CharField('aminites name2', max_length=30)
    name3 = models.CharField('aminites name3', max_length=30)
    name4 = models.CharField('aminites name4', max_length=30)
    name5 = models.CharField('aminites name5', max_length=30)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Aminit'
        verbose_name_plural = 'Aminits'

class Bedroom(models.Model):
    name = models.IntegerField('Bedroom')
    name2 = models.IntegerField('Bedroom2')
    name3 = models.IntegerField('Bedroom3')
    name4 = models.IntegerField('Bedroom4')
    name5 = models.IntegerField('Bedroom5') 
    
    
    def __int__(self):
        return self.name

class Meta:
    verbose_name = 'Bedroom'
    verbose_name_plural = 'Bedrooms'

class Bathroom(models.Model):
    name = models.IntegerField('Bathroom')
    name2 = models.IntegerField('Bathroom2')
    name3 = models.IntegerField('Bathroom3')
    name4 = models.IntegerField('Bathroom4')
    name5 = models.IntegerField('Bathroom5') 
    
    
    def __int__(self):
        return self.name

class Meta:
    verbose_name = 'Bathroom'
    verbose_name_plural = 'Bathrooms'

class Services(models.Model):
    name = models.CharField('Services name', max_length=40)
    text = models.TextField('Services text')
    img = models.ImageField('Services img', upload_to='media')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Services'
        verbose_name_plural = 'Servicess'

class StaysHotel(models.Model):


    RentShell_CHOICES = [
        ('for Rent', ' Rent'),
        ('for Shell', ' Shell')
    ]




    name = models.CharField('hotek name', max_length = 30) 
    rennt = models.CharField(max_length = 10, choices = RentShell_CHOICES, default = 'for Rent')
    img = models.ImageField('hyuranosc nakar', upload_to = 'media')
    pay = models.IntegerField('pay')
    sqft = models.IntegerField('sqrft chap')
    beds = models.IntegerField('beds')
    bats = models.IntegerField('bets')
    photo = models.IntegerField('photo')
    video = models.IntegerField('video')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'StaysHotel'
        verbose_name_plural = 'StaysHotels'




# Blog
class Blogbg(models.Model):
    name = models.CharField('blogbg name', max_length=50, blank=True)
    name2 = models.CharField('blogbg name2', max_length=50)
    img = models.ImageField('blogbg image', upload_to = 'media')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Blogbg'
        verbose_name_plural = 'Blogbgs'

class Hayvayr(models.Model):
    name = models.CharField('hayvayr name', max_length=50)
    about = models.TextField('hayrvayr name')
    img = models.ImageField('hayvayr img', upload_to='media')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Hayvayr'
        verbose_name_plural = 'Hayvayrs'


# flights
class Flights(models.Model):
    name = models.CharField('flights name', max_length= 20)
    name2 = models.CharField('flights name2', max_length= 20, null=True)
    name3 = models.CharField('flights name3', max_length= 20, null=True)
    name4 = models.CharField('flights name4', max_length= 20, null=True)
    name5 = models.CharField('flights name5', max_length= 20, null=True, blank=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Flights'
        verbose_name_plural = 'Flightss'


class Flightspay(models.Model):
    name = models.CharField('flightpays name', max_length= 20)
    name2 = models.CharField('flightpays name2', max_length= 20, null=True)
    name3 = models.CharField('flightpays name3', max_length= 20, null=True)
    name4 = models.CharField('flightpays name4', max_length= 20, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Flightspay'
        verbose_name_plural = 'Flightspays'
class Flightsrec(models.Model):
    name = models.CharField('flightsrec name', max_length= 20)
    name2 = models.CharField('flightsrec name2', max_length= 20, null=True)
   
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Flightsrec'
        verbose_name_plural = 'Flightsrecs'






    