# Generated by Django 5.0.6 on 2024-06-12 21:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_remove_documentpersonnage_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentpersonnage',
            name='DateEnreg',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
