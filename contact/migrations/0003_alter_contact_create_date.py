# Generated by Django 5.1.6 on 2025-02-24 02:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contact_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
