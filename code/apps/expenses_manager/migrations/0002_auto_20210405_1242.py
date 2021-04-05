# Generated by Django 3.0.2 on 2021-04-05 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='account',
        ),
        migrations.AddField(
            model_name='expense',
            name='currency',
            field=models.CharField(choices=[('PLN', 'Polish Złoty'), ('EUR', 'Euro'), ('GBP', 'British Pound'), ('USD', 'U.S. Dollar'), ('JPY', 'Japanese Yen'), ('CHF', 'Swiss Franc'), ('CAD', 'Canadian Dollar')], default='EUR', max_length=3),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]
