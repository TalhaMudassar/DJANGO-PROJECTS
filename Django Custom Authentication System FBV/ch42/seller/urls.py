from django.urls import path
from seller.views import seller_dashboard_view
urlpatterns = [
    path('dashboard', seller_dashboard_view, name='seller_dashboard')
]
