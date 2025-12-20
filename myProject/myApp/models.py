from django.db import models

# Create your models here.

class DepartmentModel(models.Model):
    DepartmentName=models.CharField(max_length=100,null=True)
    DepartmentLocation=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.DepartmentName
    

class DoctorModel(models.Model):
    DoctorName=models.CharField(max_length=100,null=True)
    Specialization=models.CharField(max_length=100,null=True)
    Phone=models.CharField(max_length=100,null=True)
    Email=models.EmailField(max_length=100,null=True)
    department=models.ForeignKey(DepartmentModel,max_length=100,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.DoctorName
    

class PatientModel(models.Model):
    Patientname=models.CharField(max_length=100,null=True)
    Age=models.CharField(max_length=100,null=True)
    Gender=models.CharField(max_length=100,null=True)
    Phone=models.CharField(max_length=100,null=True)
    Address=models.TextField(max_length=100,null=True)
    Doctor=models.ForeignKey(DoctorModel,max_length=100,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.Patientname+"-"+self.Doctor.DoctorName
    

class AppointmentModel(models.Model):
    patient=models.ForeignKey(PatientModel,max_length=100,null=True,on_delete=models.CASCADE)
    doctor=models.ForeignKey(DoctorModel,max_length=100,null=True,on_delete=models.CASCADE)
    appointment_date=models.DateTimeField(null=True)
    status=models.CharField(max_length=100,null=True,default='Pending')

    def __str__(self):
        return self.patient.Patientname
    
