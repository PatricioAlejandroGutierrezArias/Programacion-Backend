# Generated by Django 4.2.7 on 2023-11-16 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaInicido', models.DateField()),
                ('FechaTermino', models.DateField()),
                ('nombre', models.CharField(max_length=50)),
                ('responsable', models.CharField(max_length=50)),
                ('prioridad', models.IntegerField()),
            ],
            options={
                'db_table': 'proyecto',
            },
        ),
    ]