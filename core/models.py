from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from users.models import User
class Restaurant(models.Model):
    class Restaurant_type(models.TextChoices):
        FASTFOOD = 'FF', 'Fast Food'
        ASIAN = 'AS', 'Asian'
        ITALIAN = 'IT', 'Italian'
        GHANAIAN = 'GH', 'Ghanaian'
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=100)
    contact = models.CharField(validators=[MinLengthValidator(10), MaxLengthValidator(10)])
    email = models.EmailField(unique=True, blank=False)
    date_opened = models.DateField()
    working_hours = models.CharField(max_length=20, default='09:00am - 10:00pm')
    type = models.CharField(max_length=2, choices=Restaurant_type.choices, default='')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
