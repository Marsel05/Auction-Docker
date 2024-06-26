# Generated by Django 5.0.6 on 2024-05-09 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_car_name_car_car_name_en_car_car_name_en_en_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='car_name_en_en',
            new_name='car_name_kg',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='car_name_en_kg',
            new_name='car_name_ru',
        ),
        migrations.RemoveField(
            model_name='car',
            name='car_name_en_ru',
        ),
        migrations.AddField(
            model_name='car',
            name='car_name',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='car_name_en',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
