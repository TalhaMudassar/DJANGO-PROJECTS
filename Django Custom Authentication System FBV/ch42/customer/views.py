from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required
def customer_dashboard_view(request):
    """
    Simple dashboard page for customers.
    """
    return render(request, 'customer/dashboard.html')

@login_required
def password_change_view(request):
    """
    Change password for the logged-in user using PasswordChangeForm.
    IMPORTANT: the template must use input names:
      - old_password
      - new_password1
      - new_password2
    """
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()  # updates password and handles session invalidation
            logout(request)  # force re-login with new password
            messages.success(request, "Password changed successfully. Please log in with your new password.")
            return redirect('login')
        # If you want to surface field errors as flash messages, uncomment:
        # else:
        #     for field, errors in form.errors.items():
        #         for error in errors:
        #             messages.error(request, error)
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'customer/password_change.html', {'form': form})
