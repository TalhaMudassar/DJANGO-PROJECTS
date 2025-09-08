from django.contrib import admin
from scanner.models import QRCode
# Register your models here.
@admin.register(QRCode)
class QRCode(admin.ModelAdmin):
    list_display=['data','mobile_number']