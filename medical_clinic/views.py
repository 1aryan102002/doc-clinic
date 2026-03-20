from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import AppointmentForm

def home(request):
    return render(request, 'medical_clinic/home.html')

def about_doctor(request):
    return render(request, 'medical_clinic/about_doctor.html')

def services(request):
    return render(request, 'medical_clinic/services.html')

def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            messages.success(
                request,
                f"Appointment registered successfully. Your appointment ID is #{appointment.id}.",
            )
            return redirect("book_appointment")
    else:
        form = AppointmentForm()

    return render(request, "medical_clinic/book_appointment.html", {"form": form})
