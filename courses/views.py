from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from students.models import Student
import time
from django.utils.text import slugify


def home(request):
    return render(request, "index.html")


def course_list(request):
    courses = Course.objects.all()
    ctx = {'courses': courses}
    return render(request, 'courses/course-list.html', ctx)


def add_course(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        duration = request.POST.get('duration')
        price = request.POST.get('price')
        number = request.POST.get('number')
        start = request.POST.get('start')
        end = request.POST.get('end')

        if name and description and duration and price and number and start and end:
            slug = slugify(name) + '-' + str(int(time.time()))
            Course.objects.create(
                name=name,
                slug=slug,
                description=description,
                duration=int(duration),
                price=float(price),
                number=int(number),
                start=start,
                end=end,
            )
            return redirect('courses:list')
    return render(request, 'courses/course-create.html')


def course_detail(request, year, month, day, slug):
    course = get_object_or_404(
        Course, slug=slug, created_at__year=year, created_at__month=month, created_at__day=day
    )

    # Get students using the correct related name
    students = course.students.all()  # Use related_name

    paginator = Paginator(students, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'courses/course-detail.html', {
        'course': course,
        'page_obj': page_obj
    })



def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    students = Student.objects.filter(course)
    if request.method == "POST":
        course.delete()
        return redirect('courses:list')
    return render(request, 'courses/course-delete-confirm.html', {'course': course, 'students': students})
