from django.http import HttpResponse
from django.shortcuts import render
from requests import request

from appointments.models import Teacher

def index(request):
    return render(request, 'Boss_ERP/index.html', context=None)

def appointments_view(request):
   return render(request, 'appointments/appointments.html', context=None)

def all_teachers_view(request):
    teachers_list = []

    for i in Teacher.objects.all().values():
        teachers_list.append(i.values())
    data = {
        "teachers": teachers_list
    }

    return render(request, 'appointments/all_teachers.html', context=data)