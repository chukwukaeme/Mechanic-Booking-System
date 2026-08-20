from django.shortcuts import render
from bookings.models import Service


def home(request):

    services = Service.objects.all()[:3]

    return render(
        request,
        "core/home.html",
        {
            "services": services
        }
    )


def services(request):

    services = Service.objects.all()

    return render(
        request,
        "core/services.html",
        {
            "services": services
        }
    )


def about(request):

    return render(
        request,
        "core/about.html"
    )


def contact(request):

    return render(
        request,
        "core/contact.html"
    )