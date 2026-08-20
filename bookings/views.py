from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import timedelta

from .forms import BookingForm
from .models import Booking


@login_required
def create_booking(request):

    error_message = None

    if request.method == 'POST':

        form = BookingForm(request.POST)

        if form.is_valid():

            booking = form.save(commit=False)

            booking.customer = request.user

            start_date = booking.booking_date

            end_date = (
                start_date +
                timedelta(
                    days=booking.service.duration_days
                )
            )

            conflicting_bookings = Booking.objects.filter(
                booking_date__lt=end_date,
                end_date__gt=start_date
            )

            if conflicting_bookings.exists():

                error_message = (
                    "Sorry, mechanic is unavailable "
                    "during this period."
                )

            else:

                booking.save()

                return redirect(
                    'booking_success'
                )

    else:

        form = BookingForm()


    return render(
        request,
        'bookings/create_booking.html',
        {
            'form': form,
            'error_message': error_message
        }
    )


def booking_success(request):

    return render(
        request,
        'bookings/booking_success.html'
    )


@login_required
def my_bookings(request):

    bookings = Booking.objects.filter(
        customer=request.user
    ).order_by(
        "-created_at"
    )

    return render(
        request,
        "bookings/my_bookings.html",
        {
            "bookings": bookings
        }
    )