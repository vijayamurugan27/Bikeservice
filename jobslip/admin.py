from django.contrib import admin

from django.contrib import admin
from jobslip.models import Customer

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list=['jno','date','name','brand','model','complaint','warranty','email','contact','address']

admin.site.register(Customer)