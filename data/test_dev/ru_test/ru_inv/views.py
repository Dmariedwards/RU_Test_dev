from django.shortcuts import render
from django.http import HttpResponse
from .models import Computer
from django.http import Http404

# Create your views here.

def index(request):
	all_computers = Computer.objects.all()
	context = {'all_computers':all_computers,}
	return render(request,'ru_inv/index.html',context)

def detail(request,serial_num):
	try:
		computer = Computer.objects.get(pk =serial_num)
	except Computer.DoesNotExist:
		raise Http404("Computer model does not exist.")
	return render(request,'ru_inv/detail.html',{'computer':computer})
