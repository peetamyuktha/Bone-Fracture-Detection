from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
               path("DoctorLogin.html", views.DoctorLogin, name="DoctorLogin"),	      
               path("DoctorLoginAction", views.DoctorLoginAction, name="DoctorLoginAction"),
	       path("PatientLogin.html", views.PatientLogin, name="PatientLogin"),	      
               path("PatientLoginAction", views.PatientLoginAction, name="PatientLoginAction"),
               path("RegisterAction", views.RegisterAction, name="RegisterAction"),
               path("Register.html", views.Register, name="Register"),
               path("UploadXray.html", views.UploadXray, name="UploadXray"),	      
               path("UploadXrayAction", views.UploadXrayAction, name="UploadXrayAction"),
	       path("ViewPastResult", views.ViewPastResult, name="ViewPastResult"),	      
               path("ViewPatientReport", views.ViewPatientReport, name="ViewPatientReport"),	       
]
