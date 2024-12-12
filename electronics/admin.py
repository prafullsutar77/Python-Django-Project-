from django.contrib import admin
from .models import LaptopModel,MobileModel,TvModel
# Register your models here.
class LaptopModelAdmin(admin.ModelAdmin):
    list_display = ['modelname','modelprice','modelqnty']

class MobileModelAdmin(admin.ModelAdmin):
    list_display = ['modelname','modelprice','modelqnty']

class TvModelAdmin(admin.ModelAdmin):
    list_display = ['modelname','modelprice','modelqnty']

admin.site.register(LaptopModel,LaptopModelAdmin)
admin.site.register(MobileModel,MobileModelAdmin)
admin.site.register(TvModel,TvModelAdmin)

