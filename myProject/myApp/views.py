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
        departmentnm=request.POST.get("departmentnm")

        data=DoctorModel(
            DoctorName=name,
            Specialization=specialty,
            Phone=phone,
            Email=email,
            department=departmentnm,
        )
        data.save()
        return redirect("doctorPage")
    
    
    
    doctors=DoctorModel.objects.all()
    departments=DepartmentModel.objects.all()


    context={
        'doctors':doctors,
        'departments':departments,
    }

    return render(request,"doctorPage.html",context)


def patientPage(request):
    return render(request,"patientPage.html")

def appointmentPage(request):
    return render(request,"appointmentPage.html")

def departmentPage(request):
    return render(request,"departmentPage.html")