from django.urls import path
from scanner.views import generate_qr, scan_qr, manual_cleanup

urlpatterns = [
    path('generate/', generate_qr, name="generate_qr"),
    path('scan/', scan_qr, name="scan_qr"),
    path('cleanup/', manual_cleanup, name="manual_cleanup"),
]