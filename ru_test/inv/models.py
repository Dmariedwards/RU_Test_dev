from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.shortcuts import render, get_object_or_404,Http404

# Create your models here.
class Inventory(models.Model):
	i_name = models.CharField(max_length = 250)
	
	def __str__(self):
		return self.i_name
	def get_absolute_url(self):
		return reverse('inv:inv_index')



class Computer(models.Model):
	invent= models.ForeignKey(Inventory, null=True, blank=True,on_delete=models.CASCADE)
	manufacturer = models.CharField(max_length = 250)
	serial = models.CharField(max_length = 50)
	comments = models.CharField(max_length = 1000)

	def __str__(self):
		return self.manufacturer + "--"+ self.serial

	
		

