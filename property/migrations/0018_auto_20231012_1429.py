# Generated by Django 2.2.24 on 2023-10-12 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20231012_1428'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owner_phone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_pure_phone',
            new_name='pure_phone',
        ),
    ]
