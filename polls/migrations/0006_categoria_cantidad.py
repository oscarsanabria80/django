# Generated by Django 4.2 on 2024-01-26 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_modelo'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='Cantidad',
            field=models.IntegerField(default=0),
        ),
    ]