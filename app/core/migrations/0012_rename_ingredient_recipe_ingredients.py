# Generated by Django 3.2 on 2021-04-28 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_rename_time_miniutes_recipe_time_minutes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingredient',
            new_name='ingredients',
        ),
    ]
