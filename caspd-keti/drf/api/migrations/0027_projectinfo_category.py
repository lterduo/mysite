# Generated by Django 2.2 on 2021-01-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_remove_projectinfo_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectinfo',
            name='category',
            field=models.IntegerField(null=True),
        ),
    ]