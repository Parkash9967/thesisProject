from django.db import models


# Create your models here.


class Scholarships(models.Model):
    scholarship_name = models.CharField(max_length=100, blank=True)
    scholarship_url = models.CharField(max_length=100, blank=True)
    scholarship_university = models.CharField(max_length=100, blank=True)
    scholarship_program = models.CharField(max_length=100, blank=True)
    scholarship_deadline = models.CharField(max_length=100, blank=True)
    scholarship_country = models.CharField(max_length=100, blank=True)
    scholarship_Start_date = models.CharField(max_length=100, blank=True)
