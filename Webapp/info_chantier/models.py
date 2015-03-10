from django.db import models

# Create your models here.

class Roadwork(models.Model):
    name = models.CharField(max_length=50)
    date_start = models.DateField()
    date_end = models.DateField()
    city = models.CharField(max_length=50)
    coord = models.CharField(max_length=50)
    object = models.CharField(max_length=1000)
    description = models.CharField(max_length=5000)
    contact = models.ForeignKey('Pro')
    
class Infos_journalieres(models.Model):
    date = models.DateField()
    parking_access = models.IntegerField()
    walker_access = models.IntegerField()
    traffic_access = models.IntegerField()
    noise_access = models.IntegerField()
    
class Deviation(models.Model):
    id_roadwork = models.ForeignKey('Roadwork')
    center = models.CharField(max_length=50) 
    path = models.CharField(max_length=500)
    
class Alert(models.Model):
    id_roadwork = models.ForeignKey('Roadwork')
    timestamp = models.TimeField()
    table = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    old_value = models.CharField(max_length=100)
    new_value = models.CharField(max_length=100)
    
class Capteur(models.Model):
    timestamp = models.TimeField()
    type = models.CharField(max_length=50)
    value = models.IntegerField()
    
class Message(models.Model):
    id_user = models.ForeignKey('user')
    id_roadwork = models.ForeignKey('Roadwork')
    isAnswer = models.BooleanField(default=False)
    content = models.CharField(max_length=1000)
    
class user(models.Model):
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    levelinfo = models.IntegerField()
    
class Pro(models.Model):
    civility  = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)