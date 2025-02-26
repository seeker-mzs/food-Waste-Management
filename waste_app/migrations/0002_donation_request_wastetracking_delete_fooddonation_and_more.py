# Generated by Django 5.1.4 on 2025-02-03 09:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("waste_app", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Donation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("donor_name", models.CharField(max_length=100)),
                ("food_type", models.CharField(max_length=100)),
                ("quantity", models.PositiveIntegerField()),
                ("donation_date", models.DateField()),
                ("expiration_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Request",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("food_type", models.CharField(max_length=100)),
                ("requested_quantity", models.PositiveIntegerField()),
                ("request_date", models.DateField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WasteTracking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("wasted_quantity", models.PositiveIntegerField()),
                (
                    "reason_for_waste",
                    models.CharField(
                        choices=[
                            ("Expired", "Expired"),
                            ("Spoiled", "Spoiled"),
                            ("Overcooked", "Overcooked"),
                        ],
                        max_length=100,
                    ),
                ),
                ("waste_date", models.DateField()),
                (
                    "donation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="waste_app.donation",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="FoodDonation",
        ),
        migrations.DeleteModel(
            name="FoodRequest",
        ),
    ]
