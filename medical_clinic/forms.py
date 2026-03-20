from django import forms

from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "full_name",
            "phone",
            "email",
            "preferred_date",
            "preferred_time",
            "reason",
            "message",
        ]
        widgets = {
            "preferred_date": forms.DateInput(attrs={"type": "date"}),
            "preferred_time": forms.TimeInput(attrs={"type": "time"}),
            "message": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        base = "w-full rounded-xl border border-slate-200 bg-white px-4 py-3 text-slate-900 placeholder-slate-400 shadow-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-200"
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", base)
        self.fields["full_name"].widget.attrs.setdefault("placeholder", "Full name")
        self.fields["phone"].widget.attrs.setdefault("placeholder", "Phone number")
        self.fields["email"].widget.attrs.setdefault("placeholder", "Email (optional)")
        self.fields["reason"].widget.attrs.setdefault("placeholder", "Reason for visit (optional)")
        self.fields["message"].widget.attrs.setdefault("placeholder", "Tell us about your symptoms (optional)")
