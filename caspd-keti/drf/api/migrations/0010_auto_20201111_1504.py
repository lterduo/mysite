# Generated by Django 2.2 on 2020-11-11 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20201110_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectleader',
            name='p_id',
        ),
        migrations.RemoveField(
            model_name='projectmember',
            name='p_id',
        ),
        migrations.AddField(
            model_name='projectinfo',
            name='pid',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='projectleader',
            name='pid',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='projectmember',
            name='pid',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
