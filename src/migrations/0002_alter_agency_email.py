# Generated by Django 5.0.6 on 2024-07-12 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='email',
            field=models.EmailField(max_length=35),
        ),
    ]