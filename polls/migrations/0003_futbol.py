# Generated by Django 4.2 on 2024-01-24 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Futbol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Abr', models.CharField(max_length=4)),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
    ]