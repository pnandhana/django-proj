from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_template/', views.upload_template, name='upload_template'),
    path('upload_excel/', views.upload_excel, name='upload_excel'),
    path('generate_certificates/', views.generate_certificates, name='generate_certificates'),
]
