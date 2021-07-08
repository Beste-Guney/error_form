from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
class InterviewForm(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    age = models.CharField(max_length=100, blank=True)
    date_of_birth = models.CharField(max_length=100, blank=True)
    candidate_cv = models.FileField(null=True, blank=True)
    phone_number = models.CharField(null=True, max_length=100, blank=True)
    picture = models.FileField(null=True, blank=True)

