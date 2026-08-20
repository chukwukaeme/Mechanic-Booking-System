from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta


class Service(models.Model):

    service_name = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True,
        default=""
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    duration_days = models.IntegerField()


    def __str__(self):

        return self.service_name


class Booking(models.Model):

    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('COMPLETED', 'Completed'),
    )


    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE
    )

    car_model = models.CharField(
        max_length=100
    )

    problem_description = models.TextField()

    booking_date = models.DateField()

    end_date = models.DateField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def save(self, *args, **kwargs):

        self.end_date = (
            self.booking_date +
            timedelta(
                days=self.service.duration_days
            )
        )

        super().save(*args, **kwargs)


    def __str__(self):

        return (
            f"{self.customer.username} - "
            f"{self.service.service_name}"
        )