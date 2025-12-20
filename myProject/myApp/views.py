from django.shortcuts import render

# Create your views here.


def homePage(request):
    return render(request,"homePage.html")

def doctorPage(request):
    return render(request,"doctorPage.html")


def patientPage(request):
    return render(request,"patientPage.html")

def appointmentPage(request):
    return render(request,"appointmentPage.html")

def departmentPage(request):
    return render(request,"departmentPage.html")