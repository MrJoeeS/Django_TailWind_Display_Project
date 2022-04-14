from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Usermodel(models.Model):

    id = models.IntegerField(primary_key=True)
    first_name = models.TextField(max_length=1000)
    last_name = models.TextField(max_length=1000)
    email = models.TextField(max_length=1000, default='')
    gender = models.TextField(max_length=1000)
    ip_address = models.CharField(max_length=1000)
    
    class Meta:
        db_table = 'users'

class Datamodel(models.Model):

    id = models.IntegerField(primary_key=True)
    number = models.TextField(max_length=100)
    
    class Meta:
        db_table = 'dis'