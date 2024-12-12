from django.contrib import admin
from .models import MensWearModel,KidsWearModel,WomenWearModel
# Register your models here.
class MensWearModelAdmin(admin.ModelAdmin):
    list_display = ['modelname','modelprice','modelqnty','modelbrand']

class WomenWearModelAdmin(admin.ModelAdmin):
    list_display = ['modelname','modelprice','modelqnty','modelbrand']

class KidsWearModelAdmin(admin.ModelAdmin):
    list_display = ['modelname','modelprice','modelqnty','modelbrand']

admin.site.register(MensWearModel,MensWearModelAdmin)
admin.site.register(WomenWearModel,WomenWearModelAdmin)
admin.site.register(KidsWearModel,KidsWearModelAdmin)
