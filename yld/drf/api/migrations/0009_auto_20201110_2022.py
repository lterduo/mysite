# Generated by Django 2.2 on 2020-11-10 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20201109_2301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectinfo',
            old_name='detail',
            new_name='content',
        ),
        migrations.AddField(
            model_name='projectinfo',
            name='complete_time',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='projectinfo',
            name='result_type',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='projectinfo',
            name='total_words',
            field=models.CharField(max_length=8, null=True),
        ),
    ]