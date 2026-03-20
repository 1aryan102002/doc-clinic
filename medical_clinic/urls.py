from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-doctor/', views.about_doctor, name='about_doctor'),
    path('services/', views.services, name='services'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
]
