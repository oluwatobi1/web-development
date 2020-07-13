from django.db import models


# Create your models here.

class People(models.Model):
    first_name = models.CharField(max_length = 78)
    last_name = models.CharField(max_length = 78)
    email = models.CharField(max_length = 55)
    password = models.CharField(max_length = 45, default = 'nothing')

    def __str__(self):
        return self.first_name

class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )
