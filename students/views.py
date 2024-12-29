from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from courses.models import Course


def student_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students/student-list.html', ctx)


def add_student(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        courses = request.POST.getlist('courses')
        notes = request.POST.get('notes')
        if first_name and last_name and email and phone and courses and notes:
            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                courses=courses,
                notes=notes,
            )
            # student.courses.set(courses)
            return redirect('students:list')
    courses = Course.objects.all()
    return render(request, 'students/student-create.html', {'courses': courses})



def student_detail(request, year, month, day, slug):
    student = get_object_or_404(
        Student,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )
    return render(request, 'students/student-detail.html', {'student': student})


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('students:list')
    return render(request, 'students/student-delete-confirm.html', {'student': student})