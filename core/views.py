from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def home(request):
    return render(request, 'core/home.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'core/student_list.html', {'students': students})

def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'core/student_form.html', {'form': form})

def student_edit(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'core/student_form.html', {'form': form})

def student_delete(request, id):
    student = get_object_or_404(Student, pk=id)
    student.delete()
    return redirect('student_list')
