# Generated by Django 4.0.1 on 2022-01-18 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabib', '0006_remove_reserved_apointment_date_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reserved_apointment',
            new_name='ReservedApointment',
        ),
        migrations.DeleteModel(
            name='Apointment',
        ),
    ]
