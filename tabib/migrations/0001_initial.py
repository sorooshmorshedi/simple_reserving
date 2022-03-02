# Generated by Django 4.0.1 on 2022-01-18 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WorkTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_week_date', models.DateField()),
                ('saturday_start', models.TimeField()),
                ('saturday_end', models.TimeField()),
                ('sunday_start', models.TimeField()),
                ('sunday_end', models.TimeField()),
                ('monday_start', models.TimeField()),
                ('monday_end', models.TimeField()),
                ('tuesday_start', models.TimeField()),
                ('tuesday_end', models.TimeField()),
                ('wensday_start', models.TimeField()),
                ('wensday_end', models.TimeField()),
                ('tursday_start', models.TimeField()),
                ('tursday_end', models.TimeField()),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tabib.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Reserved_apointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('sa', 'شنبه'), ('su', '1شنبه'), ('mo', '2شنبه'), ('tu', '3شنبه'), ('we', '4شنبه'), ('tur', '5شنبه')], default='sa', max_length=3)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='tabib.doctor')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='tabib.user')),
                ('work_time', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tabib.worktime')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='tabib.user'),
        ),
        migrations.CreateModel(
            name='DayDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('sa', 'شنبه'), ('su', '1شنبه'), ('mo', '2شنبه'), ('tu', '3شنبه'), ('we', '4شنبه'), ('tur', '5شنبه')], default='sa', max_length=3)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='tabib.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Apointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='tabib.doctor')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='tabib.user')),
            ],
        ),
    ]