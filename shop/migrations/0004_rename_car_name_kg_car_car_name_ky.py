# Generated by Django 5.0.6 on 2024-05-12 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_car_name_en_en_car_car_name_kg_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='car_name_kg',
            new_name='car_name_ky',
        ),
    ]
