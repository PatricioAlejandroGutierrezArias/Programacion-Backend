# Generated by Django 4.2.7 on 2023-11-16 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_6_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyecto',
            old_name='FechaInicido',
            new_name='fechaInicio',
        ),
        migrations.RenameField(
            model_name='proyecto',
            old_name='FechaTermino',
            new_name='fechaTermino',
        ),
    ]
