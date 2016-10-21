from django.shortcuts import render, get_object_or_404,Http404
from .models import Computer, Inventory

# Create your views here.
def inv_index(request):
	all_inventories = Inventory.objects.all()
	context = {'all_inventories':all_inventories}
	return render(request,'inv/inv_index.html',context)

def comp_index(request,inv_id):
	inve = get_object_or_404(Inventory, pk = inv_id)
	return render(request,'inv/index.html',{'inve':inve})

def detail(request,serial_num, inv_id):
	inve = get_object_or_404(Inventory, pk = inv_id)
	try:
		computer = inve.computer_set.get(pk = serial_num)

	except (KeyError, Computer.DoesNotExist):
		raise Http404 ("Computer_id does not exist")
		# return render(request,'inv/index.html',{'inve':inve})
	return render(request,'inv/detail.html',{'computer':computer})
