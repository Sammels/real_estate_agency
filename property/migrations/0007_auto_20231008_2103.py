# Generated by Django 2.2.24 on 2023-10-08 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_complaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='text',
            field=models.TextField(verbose_name='Текст жалобы'),
        ),
    ]
