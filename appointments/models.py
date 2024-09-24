from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=32)
    subject = models.CharField(max_length=32)
    hourly_rate = models.IntegerField()

    def __str__(self):
        return str(self.name) + ' ' + str(self.subject)


class Student(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return str(self.name) + ' ' + str(self.surname)
