from django.db import models
from django.db.models.functions import Now


class Subject(models.Model):
    subject_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.subject_name)


class Teacher(models.Model):
    first_name = models.CharField(max_length=32, default="John")
    last_name = models.CharField(max_length=32,  default="Dow")
    phone_number = models.CharField(max_length=12, default="8-800-555-35-35")
    hourly_rate = models.IntegerField()

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)


class Student(models.Model):
    first_name = models.CharField(max_length=32, default="John")
    last_name = models.CharField(max_length=32,  default="Dow")
    phone_number = models.CharField(max_length=12, default="8-800-555-35-35")

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)


class TeacherSubject(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)


class Appointment(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher_subject_id = models.ForeignKey(TeacherSubject, on_delete=models.CASCADE)
    class_time = models.DateTimeField(db_default=Now())
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)




