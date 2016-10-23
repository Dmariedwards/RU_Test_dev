from django.conf.urls import url
from . import views
from .models import Inventory, Computer




app_name = 'inv'

urlpatterns = [
	#main page
    url(r'^$', views.IndexView.as_view(), name = 'inv_index'),

    # inv/inv _id
	url(r'^(?P<inv_id>[0-9]+)/$',views.comp_index, name ='comp_index'),

	#inv.id/computer_id
	url(r'^(?P<inv_id>[0-9]+)/(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name ='details'),

	#inventory/add
	url(r'^inventory/add/$', views.InventoryCreate.as_view(), name='add-inventory'),

	#update/inv_id
	url(r'^update/(?P<pk>[0-9]+)/$', views.InventoryUpdate.as_view(), name='update_inventory'),

	#inv_id/delete
	url(r'^(?P<pk>[0-9]+)/delete/$', views.InventoryDelete.as_view(), name='delete_inventory'),

	#inv_id/create_computer
	url(r'^(?P<inv_id>[0-9]+)/add_computer/$', views.create_computer, name='add-computer'),

	#inv_id/ comp_id/delete_computer/
	url(r'^(?P<inv_id>[0-9]+)/delete_computer/(?P<comp_id>[0-9]+)/$', views.delete_computer, name='delete_computer'),

	# #inv_id/delete_computer/ comp_id
	url(r'^update_comp/(?P<pk>[0-9]+)/(?P<slug>[0-9]+)/$', views.ComputerUpdate.as_view(), name='update_computer'),

	# url(r'^(?P<inv_id>[0-9]+)/update_comp/(?P<comp_id>[0-9]+)/$', views.update_computer, name='update_computer'),


	

]