from django.contrib import admin
from .models import Booking, Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "service_name",
        "price",
        "duration_days",
    )

    search_fields = (
        "service_name",
    )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        "customer",
        "service",
        "car_model",
        "booking_date",
        "end_date",
        "status",
    )

    list_filter = (
        "status",
        "booking_date",
    )

    search_fields = (
        "customer__username",
        "service__service_name",
        "car_model",
    )

    list_editable = (
        "status",
    )

    ordering = (
        "-booking_date",
    )