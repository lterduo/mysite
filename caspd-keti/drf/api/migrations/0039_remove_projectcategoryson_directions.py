# Generated by Django 2.2 on 2021-02-16 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_projectcategoryson_directions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectcategoryson',
            name='directions',
        ),
    ]