from django.db import models
from django.contrib.auth.models import User

class Donation(models.Model):
    donor_name = models.CharField(max_length=100)
    food_type = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    donation_date = models.DateField()  # Remove auto_now_add=True if you want the user to input it
    expiration_date = models.DateField()

    def __str__(self):
        return f"{self.food_type} - {self.donor_name}"


class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_type = models.CharField(max_length=100)
    requested_quantity = models.PositiveIntegerField()
    request_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.food_type} - {self.requested_quantity} units (Requested by {self.user.username})"

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
