from django.contrib import admin
from django.utils import timezone

from .models import Appointment


class AppointmentDayFilter(admin.SimpleListFilter):
    title = "day"
    parameter_name = "day"

    def lookups(self, request, model_admin):
        return [
            ("today", "Today"),
            ("tomorrow", "Tomorrow"),
            ("next_7", "Next 7 days"),
        ]

    def queryset(self, request, queryset):
        value = self.value()
        if not value:
            return queryset

        today = timezone.localdate()
        if value == "today":
            return queryset.filter(preferred_date=today)
        if value == "tomorrow":
            return queryset.filter(preferred_date=today + timezone.timedelta(days=1))
        if value == "next_7":
            return queryset.filter(
                preferred_date__gte=today,
                preferred_date__lte=today + timezone.timedelta(days=7),
            )
        return queryset


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    date_hierarchy = "preferred_date"
    list_display = (
        "id",
        "full_name",
        "phone",
        "email",
        "date_of_birth",
        "preferred_date",
        "preferred_time",
        "created_at",
    )
    list_filter = (AppointmentDayFilter, "preferred_date", "created_at")
    search_fields = ("full_name", "phone", "email", "reason", "message")
    readonly_fields = ("created_at",)
    ordering = ("preferred_date", "preferred_time", "-created_at")
    list_per_page = 50
