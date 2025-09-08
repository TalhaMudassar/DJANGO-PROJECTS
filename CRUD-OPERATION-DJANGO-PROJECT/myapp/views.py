from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Student
from .forms import StudentForm  # Change here

class Home(View):
    def get(self, request):
        stu_data = Student.objects.all()
        return render(request, 'core/home.html', {'studata': stu_data})

class AddStudent(View):
    def get(self, request):
        fm = StudentForm()  # Change here
        return render(request, 'core/add-student.html', {'form': fm})
    
    def post(self, request):
        fm = StudentForm(request.POST)  # Change here
        if fm.is_valid():
            fm.save()
            return redirect('/')
        return render(request, 'core/add-student.html', {'form': fm})

class DeleteaStudent(View):
    def post(self, request):
        student_id = request.POST.get('id')
        studata = get_object_or_404(Student, id=student_id)
        studata.delete()
        return redirect('/')
    
class Editstudent(View):
    def get(self, request, id):
        stu = Student.objects.get(id=id)
        fm = StudentForm(instance=stu)  # Change here
        return render(request, 'core/edit-student.html', {'form': fm})

    def post(self, request, id):
        stu = Student.objects.get(id=id)
        fm = StudentForm(request.POST, instance=stu)  # Change here
        if fm.is_valid():
            fm.save()
            return redirect('/')
        return render(request, 'core/edit-student.html', {'form': fm})
