from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from courses.models import Course


def student_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students/student-list.html', ctx)\


def add_student(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        courses = request.POST.getlist('courses')  # Use getlist to handle multiple course selections

        if first_name and last_name and email and phone and courses:
            student = Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
            )
            student.courses.set(courses)  # Assign selected courses to the student
            return redirect('students:list')

    courses = Course.objects.all()  # Fetch all available courses
    return render(request, 'students/student-create.html', {'courses': courses})