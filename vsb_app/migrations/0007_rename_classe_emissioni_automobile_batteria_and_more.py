# Generated by Django 4.0.2 on 2022-04-10 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vsb_app', '0006_alter_ordine_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='automobile',
            old_name='classe_emissioni',
            new_name='batteria',
        ),
        migrations.RemoveField(
            model_name='automobile',
            name='cambio',
        ),
        migrations.RemoveField(
            model_name='automobile',
            name='numero_marce',
        ),
    ]
