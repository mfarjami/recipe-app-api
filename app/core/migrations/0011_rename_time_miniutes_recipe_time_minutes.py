# Generated by Django 3.2 on 2021-04-28 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='time_miniutes',
            new_name='time_minutes',
        ),
    ]
