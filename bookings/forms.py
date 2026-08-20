from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):

    class Meta:

        model = Booking

        fields = [
            'service',
            'car_model',
            'problem_description',
            'booking_date',
        ]

        widgets = {

            'booking_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'problem_description': forms.Textarea(
                attrs={
                    'rows': 4
                }
            ),
        }