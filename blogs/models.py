from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
def __str__(self): #magic method
     return self.name
class Blog(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=0) 
    
def __str__(self): #magic method
     return self.name
