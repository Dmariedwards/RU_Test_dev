from django.db import models

# Create your models here.



class Computer(models.Model):
	Manufacturer = models.CharField(max_length = 250)
	Serial = models.IntegerField()
	Comments = models.CharField(max_length = 1000)