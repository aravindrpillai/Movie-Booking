# Generated by Django 5.0.6 on 2024-07-06 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customers_id', models.UUIDField(unique=True)),
                ('full_name', models.CharField(max_length=100, null=True)),
                ('mobile_number', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'verbose_name': 'customers',
                'db_table': 'customers',
            },
        ),
    ]
