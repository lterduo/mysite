# Generated by Django 2.2 on 2021-02-16 11:20

from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0037_auto_20210117_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectcategoryson',
            name='directions',
            field=django_mysql.models.JSONField(default=dict),
        ),
    ]
