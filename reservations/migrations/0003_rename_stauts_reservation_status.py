# Generated by Django 3.2.5 on 2021-08-09 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20210808_1421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='stauts',
            new_name='status',
        ),
    ]
