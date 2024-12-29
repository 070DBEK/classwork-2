from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from students.base_model import BaseModel


class Course(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()  # e.g., weeks
    price = models.DecimalField(max_digits=10, decimal_places=2)
    number = models.IntegerField()
    start = models.DateField()
    end = models.DateField()


    def __str__(self):
        return {self.name}


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)


    def get_detail_url(self):
        return reverse('courses:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])
