from django.contrib import admin
from myApp.models import *

# Register your models here.
admin.site.register(DepartmentModel)
admin.site.register(DoctorModel)
admin.site.register(PatientModel)
admin.site.register(AppointmentModel)