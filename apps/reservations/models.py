from django.db import models
from core.models import Restaurant
from django.core.validators import MinLengthValidator, MaxLengthValidator
class Reservations(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'Pending', 'Pending'
        CONFIRMED = 'Confirmed', 'Confirmed'
        COMPLETED = 'Completed', 'Completed'
        CANCELLED = 'Cancelled', 'Cancelled'
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100, null=False, blank=False)
    guest_phone = models.CharField(validators=[MinLengthValidator(10), MaxLengthValidator(10)], null=False, blank=False)
    guest_email = models.EmailField()
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    guest_size = models.PositiveIntegerField(null=False, blank=False)
    special_note = models.TextField(max_length=100)
    status = models.CharField(max_length=10, choices=StatusChoices.choices, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reservation for {self.guest_name}"