# Generated by Django 3.0.2 on 2021-04-25 17:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("categories", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Limit",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("limit_value", models.DecimalField(decimal_places=2, max_digits=15)),
                ("current_spent", models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                (
                    "period",
                    models.CharField(
                        choices=[("D", "Daily"), ("W", "Weekly"), ("M", "Monthly"), ("Y", "Yearly")],
                        default="W",
                        max_length=1,
                    ),
                ),
                ("start_date", models.DateField()),
                (
                    "category",
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="categories.Category"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
