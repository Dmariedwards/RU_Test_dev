from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Inventory(models.Model):
	i_name = models.CharField(max_length = 250)
	
	def __str__(self):
		return self.i_name



class Computer(models.Model):
	invent= models.ForeignKey(Inventory, on_delete=models.CASCADE)
	manufacturer = models.CharField(max_length = 250)
	serial = models.CharField(max_length = 50)
	comments = models.CharField(max_length = 1000)

	def __str__(self):
		return self.manufacturer + "--"+ self.serial
