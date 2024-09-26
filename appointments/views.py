from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'Boss_ERP/index.html', context=None)

def appointments_view(request):
   return render(request, 'appointments/appointments.html', context=None)