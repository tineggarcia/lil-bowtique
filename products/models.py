from django.db import models

# Create your models here.

class Category(models.Model):
    value_name = models.CharField(max_length=60)
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=300, null=True, blank=True)

    def __value_name__(self):
        return self.value_name

    def __cat_name__(self):
        return self.name

    def __cat_desc__(self):
        return self.description
