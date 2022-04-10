# Generated by Django 4.0.2 on 2022-04-10 14:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vsb_app', '0008_alter_automobile_batteria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automobile',
            name='peso_a_vuoto',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(500), django.core.validators.MaxValueValidator(3000)]),
        ),
    ]