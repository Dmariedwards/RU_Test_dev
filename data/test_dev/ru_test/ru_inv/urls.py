from django.conf.urls import url

from . import views

urlpatterns = [
	# /Computer/
	url(r'^$', views.index, name = 'index'),

	# /Computer/id
	url(r'^(?P<serial_num>[0-9]+)/$',views.detail, name ='details'),
]
