# Generated by Django 4.0.2 on 2022-03-27 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vsb_app', '0002_automobile_data_registrazione'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automobile',
            name='carburante',
            field=models.CharField(blank=True, choices=[(None, 'Seleziona'), ('Hybrid', 'Hybrid'), ('Elettrico', 'Elettrico')], max_length=100, null=True),
        ),
    ]