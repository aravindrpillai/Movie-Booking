# Generated by Django 5.0.6 on 2024-07-10 20:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_id', models.CharField(max_length=4, unique=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeCredentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=40)),
                ('pwd_last_updated', models.DateField()),
                ('failed_attempts', models.IntegerField(default=0)),
                ('locked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_id', models.CharField(max_length=6, unique=True)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=7)),
                ('maps_url', models.URLField(null=True)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='src.agency')),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=10, unique=True)),
                ('fullname', models.CharField(max_length=40)),
                ('photo', models.CharField(max_length=100, null=True)),
                ('doj', models.DateField()),
                ('lwd', models.DateField(null=True)),
                ('active', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=40, null=True, unique=True)),
                ('mobile', models.CharField(max_length=10, unique=True)),
                ('mobile_verified', models.BooleanField(default=False)),
                ('email_verified', models.BooleanField(default=False)),
                ('employee_credential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.employeecredentials')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeAssociation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('roles', models.JSONField(null=True)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='src.agency')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='src.branches')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.employees')),
            ],
        ),
        migrations.CreateModel(
            name='Screens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='src.branches')),
            ],
        ),
    ]
