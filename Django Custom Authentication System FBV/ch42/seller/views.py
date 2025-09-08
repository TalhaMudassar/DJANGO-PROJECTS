from django.shortcuts import render

def seller_dashboard_view(request):
    """
    Simple seller dashboard page.
    """
    return render(request, 'seller/dashboard.html')
