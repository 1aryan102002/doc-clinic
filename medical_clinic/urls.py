from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-doctor/', views.about_doctor, name='about_doctor'),
    path('services/', views.services, name='services'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),

    path('home.html', views.home, name='home_html'),
    path('about-doctor.html', views.about_doctor, name='about_doctor_html'),
    path('about_doctor.html', views.about_doctor, name='about_doctor_html_underscore'),
    path('services.html', views.services, name='services_html'),
    path('book-appointment.html', views.book_appointment, name='book_appointment_html'),
    path('book_appointment.html', views.book_appointment, name='book_appointment_html_underscore'),
]
