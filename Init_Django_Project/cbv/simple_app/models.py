from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length = 150)
    location = models.CharField(max_length = 120)
    owner = models.CharField(max_length = 120)

    def __str__(self):
        return self.name

class Student(models.Model):

    daycare = 'DC'
    kindergarten = 'KG'
    primary = 'PRY'
    junior_sec = 'JSS'
    senior_sec = 'SSS'


    level_in_choices = [
    (daycare, 'Day Care'),
    (kindergarten, 'Kindergarten'),
    (primary, 'Primary'),
    (junior_sec, 'Junior Secondary'),
    (senior_sec, 'Senior Secondary')
    ]

    student_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name = 'student')
    grade_level = models.CharField(max_length =3, choices = level_in_choices,
                                    default = daycare)
    def __str__(self):
        return self.student_name
