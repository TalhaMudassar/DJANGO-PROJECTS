from django.shortcuts import render, redirect, get_object_or_404
from student.forms import ProfileForm
from student.models import Profile

# Home view - show all candidates and handle form submission
def Home(request):
    candidates = Profile.objects.all()

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Home')  # make sure 'Home' is the correct URL name
    else:
        form = ProfileForm()  # only create a blank form if GET request

    return render(request, 'student/home.html', {'form': form, 'candidates': candidates})


# Candidate detail view - show details of one candidate
def candidate_detail(request, pk):
    candidate = get_object_or_404(Profile, pk=pk)  # safer than Profile.objects.get()
    return render(request, 'student/candidate.html', {'candidate': candidate})
