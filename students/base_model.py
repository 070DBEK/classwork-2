from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # Object creation time
    updated_at = models.DateTimeField(auto_now=True)      # Object update time
    slug = models.SlugField(unique=True, blank=True)


    class Meta:
        abstract = True  # This model will not create a table in the database
