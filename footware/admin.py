from django.contrib import admin
from .models import SliperModel,ShoesModel,SportsModel
# Register your models here.
class SliperModelAdmin(admin.ModelAdmin):
    list_display = ['modelname','modelcolor','modelsize','modelprice','modelqnty']

class ShoesModelAdmin(admin.ModelAdmin):
    list_display = ['modelname','modelcolor','modelsize','modelprice','modelqnty']

class SportsModelAdmin(admin.ModelAdmin):
    list_display = ['modelname','modelcolor','modelsize','modelprice','modelqnty']

admin.site.register(SliperModel,SliperModelAdmin)
admin.site.register(SportsModel,SportsModelAdmin)
admin.site.register(ShoesModel,ShoesModelAdmin)