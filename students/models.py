from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from courses.models import Course
from students.base_model import BaseModel


class Student(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    courses = models.ManyToManyField(Course, related_name="students")


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name, self.last_name)
        super(Student, self).save(*args, **kwargs)


    def get_detail_url(self):
        return reverse('students:student_detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])