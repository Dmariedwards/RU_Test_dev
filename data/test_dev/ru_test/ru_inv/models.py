from django.db import models


class Computer(models.Model):
	manufacturer = models.CharField(max_length = 250)
	serial = models.CharField(max_length = 50)
	comments = models.CharField(max_length = 1000)

	def __str__(self):
		return self.manufacturer + "--"+ self.serial