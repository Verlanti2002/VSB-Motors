# Generated by Django 4.0.2 on 2022-03-20 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vsb_app', '0006_alter_automobile_targa_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='automobile',
            name='cambio',
            field=models.CharField(choices=[('', 'Seleziona'), ('A', 'Manuale'), ('M', 'Automatico')], default='Manuale', max_length=1),
        ),
    ]
