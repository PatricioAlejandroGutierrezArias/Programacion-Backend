# Generated by Django 4.2.7 on 2023-12-15 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gutierrez_P_Finalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutorProyecto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80)),
                ('carrera', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=50)),
            ],
            options={
                'db_table': 'AutorProyecto',
            },
        ),
    ]
