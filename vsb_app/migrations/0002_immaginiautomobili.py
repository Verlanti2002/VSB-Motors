# Generated by Django 4.0.2 on 2022-03-19 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vsb_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImmaginiAutomobili',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('immagine', models.ImageField(upload_to='images/%Y/%m/%d')),
                ('automobile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='immagini', to='vsb_app.automobile')),
            ],
            options={
                'verbose_name_plural': 'immagini',
                'db_table': 'vsb_app_immaginiAutomobili',
            },
        ),
    ]
