from datetime import datetime, timedelta

from django import forms
from django.utils import timezone

from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "full_name",
            "phone",
            "email",
            "date_of_birth",
            "preferred_date",
            "preferred_time",
            "reason",
            "message",
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "preferred_date": forms.DateInput(attrs={"type": "date"}),
            "preferred_time": forms.TimeInput(attrs={"type": "time", "step": 600}),
            "message": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        base = "w-full rounded-xl border border-slate-200 bg-white px-4 py-3 text-slate-900 placeholder-slate-400 shadow-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-200"
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", base)

        today = timezone.localdate()
        self.fields["date_of_birth"].required = True
        self.fields["preferred_time"].required = True
        self.fields["preferred_date"].widget.attrs.setdefault("min", today.isoformat())
        self.fields["date_of_birth"].widget.attrs.setdefault("max", today.isoformat())

        self.fields["full_name"].widget.attrs.setdefault("placeholder", "Full name")
        self.fields["phone"].widget.attrs.setdefault("placeholder", "Phone number")
        self.fields["email"].widget.attrs.setdefault("placeholder", "Email (optional)")
        self.fields["date_of_birth"].widget.attrs.setdefault("placeholder", "Date of birth")
        self.fields["reason"].widget.attrs.setdefault("placeholder", "Reason for visit (optional)")
        self.fields["message"].widget.attrs.setdefault("placeholder", "Tell us about your symptoms (optional)")

    def clean(self):
        cleaned_data = super().clean()
        today = timezone.localdate()

        date_of_birth = cleaned_data.get("date_of_birth")
        if date_of_birth and date_of_birth > today:
            self.add_error("date_of_birth", "Date of birth cannot be in the future.")

        preferred_date = cleaned_data.get("preferred_date")
        preferred_time = cleaned_data.get("preferred_time")

        if preferred_date and preferred_date < today:
            self.add_error("preferred_date", "Preferred date cannot be in the past.")

        if preferred_date and preferred_time:
            now = timezone.localtime().replace(tzinfo=None)
            selected_dt = datetime.combine(preferred_date, preferred_time)
            if preferred_date == today and selected_dt < now:
                self.add_error("preferred_time", "Preferred time cannot be in the past.")

            buffer_minutes = 10
            min_gap = timedelta(minutes=buffer_minutes)
            existing = Appointment.objects.filter(
                preferred_date=preferred_date,
                preferred_time__isnull=False,
            )
            if self.instance and self.instance.pk:
                existing = existing.exclude(pk=self.instance.pk)

            for appt in existing.only("preferred_time"):
                if appt.preferred_time is None:
                    continue
                existing_dt = datetime.combine(preferred_date, appt.preferred_time)
                if abs(selected_dt - existing_dt) < min_gap:
                    self.add_error(
                        "preferred_time",
                        f"Please choose a time at least {buffer_minutes} minutes away from other appointments.",
                    )
                    break

        return cleaned_data
