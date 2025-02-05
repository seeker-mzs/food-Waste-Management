from django.core.management.base import BaseCommand
from waste_app.models import Donation
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Fix invalid donor foreign key references'

    def handle(self, *args, **kwargs):
        # Find invalid donations with a non-existent donor
        invalid_donors = Donation.objects.exclude(donor__in=User.objects.all())

        # Fix or remove the invalid records
        for donation in invalid_donors:
            self.stdout.write(f"Fixing donation with ID {donation.id}...")
            donation.donor = User.objects.get(id=1)  # Replace with a valid user ID
            donation.save()

        self.stdout.write(self.style.SUCCESS('Successfully fixed invalid donors.'))
