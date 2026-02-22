from django.db import models

class StudentPerformance(models.Model):
    gender = models.CharField(max_length=32)
    race_ethnicity = models.CharField(max_length=50)
    parental_level_of_education =  models.CharField(max_length=50)
    lunch = models.CharField(max_length=32)
    test_preparation_course = models.CharField(max_length=50)
    reading_score = models.IntegerField()
    math_score = models.IntegerField()
