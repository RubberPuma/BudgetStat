# Generated by Django 3.0.2 on 2021-04-11 16:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Limit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit_value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('current_spent', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('period', models.CharField(choices=[('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly'), ('Y', 'Yearly')], default='W', max_length=1)),
                ('start_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='expenses_manager.Category')),
            ],
        ),
    ]