from django import forms
from .models import Inventory, Computer





class ComputerForm(forms.ModelForm):
	class Meta:
    		model = Computer
		fields = ['manufacturer', 'serial', 'comments']