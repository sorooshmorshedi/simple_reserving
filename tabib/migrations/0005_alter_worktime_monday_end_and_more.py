# Generated by Django 4.0.1 on 2022-01-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabib', '0004_alter_daydetail_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worktime',
            name='monday_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='worktime',
            name='monday_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='worktime',
            name='saturday_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='worktime',
            name='saturday_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='worktime',
            name='sunday_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='worktime',
            name='sunday_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='worktime',
            name='tuesday_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='worktime',
            name='tuesday_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='worktime',
            name='tursday_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='worktime',
            name='tursday_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='worktime',
            name='wensday_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='worktime',
            name='wensday_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
