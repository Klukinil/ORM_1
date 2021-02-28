from django.contrib import admin
from .models import Phone

class PhoneAdmin(admin.ModelAdmin):
    pass
# Register your models here.

admin.site.register(Phone, PhoneAdmin)