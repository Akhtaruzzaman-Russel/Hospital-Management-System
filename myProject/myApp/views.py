from django.shortcuts import render, redirect
from myApp.models import *

# Create your views here.


def homePage(request):
    return render(request,"homePage.html")

def doctorPage(request):
    if request.method=="POST":
        name=request.POST.get("name")
        specialty=request.POST.get("specialty")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        department_id=request.POST.get("department_id")
        department_name=DepartmentModel.objects.get(id=department_id)

        data=DoctorModel(
            DoctorName=name,
            Specialization=specialty,
            Phone=phone,
            Email=email,
            department=department_name,
        )
        data.save()
        return redirect("doctorPage")
    
    
    doctors=DoctorModel.objects.all()
    departments=DepartmentModel.objects.all()


    context={
        'doctors':doctors,
        'departments':departments,
    }

    return render(request,"doctorPage.html", context)


def patientPage(request):
    if request.method=="POST":
        Patient_Name=request.POST.get("Patient_Name")
        age=request.POST.get("age")
        gender=request.POST.get("gender")
        phone=request.POST.get("Patient_Name")
        address=request.POST.get("address")
        doctor_id=request.POST.get("doctor_id")
        doctor_name=DoctorModel.objects.get(id=doctor_id)

        PatientModel.objects.create(
            Patientname=Patient_Name,
            Age=age,
            Gender=gender,
            Phone=phone,
            Address=address,
            Doctor=doctor_name
        )
        return redirect("patientPage")
    
    patient_data=PatientModel.objects.all()
    doctors=DoctorModel.objects.all()

    context={
        'patient_data':patient_data,
        'doctors':doctors
    }

    return render(request,"patientPage.html", context)



def appointmentPage(request):
    return render(request,"appointmentPage.html")

def departmentPage(request):
    return render(request,"departmentPage.html")