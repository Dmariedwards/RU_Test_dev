from django.contrib import admin
from .models import Inventory, Computer
# Register your models here.
admin.site.register(Computer)
admin.site.register(Inventory)