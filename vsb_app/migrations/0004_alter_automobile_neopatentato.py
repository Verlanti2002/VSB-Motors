# Generated by Django 4.0.2 on 2022-04-09 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vsb_app', '0003_alter_automobile_concessionaria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automobile',
            name='neopatentato',
            field=models.CharField(blank=True, choices=[(None, 'Neopatentato'), ('Si', 'Si'), ('No', 'No')], max_length=100, null=True),
        ),
    ]
