from pyexpat import model
from turtle import position
from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    
class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100,null=False)
    description = models.TextField(max_length=500,default='Write something...')
    mobile = models.CharField(max_length=15,default=False)
    date_created = models.DateTimeField(blank=True,default=False)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    