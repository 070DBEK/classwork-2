from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from courses.models import Course
from students.base_model import BaseModel


class Student(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    courses = models.ForeignKey(Course, related_name='students', on_delete=models.CASCADE)
    notes = models.TextField()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name, self.last_name)
        super(Student, self).save(*args, **kwargs)


    def get_detail_url(self):
        return reverse('students:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])