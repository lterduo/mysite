# Generated by Django 2.2 on 2021-01-07 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20201122_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='duty_level',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
