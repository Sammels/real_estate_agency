# Generated by Django 2.2.24 on 2023-10-10 17:23

from django.db import migrations

def link_owner_and_flat(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all()
    owners = Owner.objects.all()

    for owner in owners.iterator():
        owner_flats = list(flats.filter(owner=owner.name, owner_pure_phone=owner.owner_pure_phone))
        owner.flats.set(owner_flats)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20231010_2048'),
    ]

    operations = [
        migrations.RunPython(link_owner_and_flat)
    ]
