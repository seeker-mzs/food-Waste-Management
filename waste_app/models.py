from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Donation(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    food_type = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    donation_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()
    
    def __str__(self):
        return f"{self.food_type} - Donated by {self.donor.username}"


class Request(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="food_requests",
        verbose_name="Requested by"
    )
    food_type = models.CharField(
        max_length=100, 
        verbose_name="Type of Food"
    )
    requested_quantity = models.PositiveIntegerField(
        verbose_name="Requested Quantity (kg)"
    )
    request_date = models.DateField(
        auto_now_add=True, 
        verbose_name="Request Date"
    )

    def __str__(self):
        return f"{self.food_type} - {self.requested_quantity} kg (Requested by {self.user.username})"

class WasteTracking(models.Model):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    wasted_quantity = models.PositiveIntegerField()
    reason_for_waste = models.CharField(
        max_length=100,
        choices=[
            ('Expired', 'Expired'),
            ('Spoiled', 'Spoiled'),
            ('Overcooked', 'Overcooked'),
        ]
    )
    waste_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.donation.food_type} - {self.wasted_quantity} units (Wasted on {self.waste_date})"
