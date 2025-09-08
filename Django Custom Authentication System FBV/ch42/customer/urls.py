from django.urls import path
from customer.views import customer_dashboard_view, password_change_view

urlpatterns = [
    path('dashboard', customer_dashboard_view, name='customer_dashboard'),
    path('password-change/', password_change_view, name='password_change'),
]
