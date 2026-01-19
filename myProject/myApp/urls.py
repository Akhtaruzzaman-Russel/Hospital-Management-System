
from django.contrib import admin
from django.urls import path,include
from myApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage',homePage, name="homePage"),
    path('doctorPage/',doctorPage, name="doctorPage"),
    path('patientPage/',patientPage, name="patientPage"),
    path('appointmentPage/',appointmentPage, name="appointmentPage"),
    path('departmentPage/',departmentPage, name="departmentPage"),
]
