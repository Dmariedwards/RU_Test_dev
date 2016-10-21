from django.conf.urls import url
from . import views


urlpatterns = [
	#main page
    url(r'^$', views.inv_index, name = 'inv_index'),
    # inv/inv _id
	url(r'^(?P<inv_id>[0-9]+)/$',views.comp_index, name ='comp_index'),
	#inv.id/computer_id
	url(r'^(?P<inv_id>[0-9]+)/(?P<serial_num>[0-9]+)/$',views.detail, name ='details'),

]