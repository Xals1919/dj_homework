# Generated by Django 4.2.7 on 2024-01-20 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_measurement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='image',
            field=models.ImageField(blank=True, max_length=500, upload_to=''),
        ),
    ]