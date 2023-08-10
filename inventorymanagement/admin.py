from django.contrib import admin
from .models import Inventory,Category,Reorder
# Register your models here.

admin.site.register(Inventory) 
admin.site.register(Category) 
admin.site.register(Reorder) 
