from django.contrib import admin
from uc.models import UnderConstruction
# Register your models here.

@admin.register(UnderConstruction)
class UnderConstructionAdmin(admin.ModelAdmin):
    list_display=['id','uc_note','uc_duration','is_under_construction']
    fields = ('uc_note','uc_duration','is_under_construction')
