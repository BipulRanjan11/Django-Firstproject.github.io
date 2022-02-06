from django.db import models

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('datepublished')


class Student(models.Model):
    std_name=models.CharField(max_length=200)
    std_id=models.IntegerField(default=0)

