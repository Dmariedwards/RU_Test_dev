from django.shortcuts import render, get_object_or_404,Http404, HttpResponseRedirect
from .models import Inventory, Computer
from django.views import generic
from .forms import ComputerForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

def comp_index(request,inv_id):
	inve = get_object_or_404(Inventory, pk = inv_id)
	return render(request,'inv/index.html',{'inve':inve})


def create_computer(request, inv_id):
    form = ComputerForm(request.POST)
    inve = get_object_or_404(Inventory, pk=inv_id)
    if form.is_valid():
        computers = inve.computer_set.all()
        for s in computers:
            if s.manufacturer == form.cleaned_data.get("manufacturer") and s.serial == form.cleaned_data.get("serial"):
                context = {
                    'inve': inve,
                    'form': form,
                    'error_message': 'You already added that computer',
                }
                return render(request, 'inv/computer_form.html', context)
        computer = form.save(commit=False)
        computer.invent = inve
      
        computer.save()
        return  HttpResponseRedirect('/' + str(inv_id))
    else:
		context = {'inve': inve,'form': form,}
		return render(request,'inv/computer_form.html', context)





class IndexView(generic.ListView):
	"""docstring for Index_view"""
	template_name = 'inv/inv_index.html'

	def get_queryset(self):
		return Inventory.objects.all()

class DetailView(generic.DetailView):
	model = Computer
	template_name = 'inv/detail.html'

class InventoryUpdate(UpdateView):
	model = Inventory
	fields = ["i_name"]

class InventoryCreate(CreateView):
	model = Inventory
	fields = ["i_name"]

class InventoryDelete(DeleteView):
	model = Inventory
	success_url = reverse_lazy('inv:inv_index')




def delete_computer(request, inv_id, comp_id):
	inve = get_object_or_404(Inventory, pk=inv_id)
    	computer = inve.computer_set.filter(id = comp_id)
    	computer.delete()	
	
    	return HttpResponseRedirect('/' + str(inv_id))

class ComputerUpdate(UpdateView):
	model = Computer
	form_class = ComputerForm
	fields = ["manufacturer", "serial", "comments"]
	template_name = 'inv/computer_form.html'
	success_url = reverse_lazy('inv:index')


