from django.contrib import admin
from .models import contact

# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display=('uname','email','address','phone','datetime','message')
admin.site.register(contact,contactAdmin)