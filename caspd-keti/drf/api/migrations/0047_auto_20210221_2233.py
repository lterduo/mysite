# Generated by Django 2.2 on 2021-02-21 22:33

from django.db import migrations
import django_jsonfield_backport.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0046_auto_20210221_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bank',
            field=django_jsonfield_backport.models.JSONField(help_text='银行账号', null=True),
        ),
    ]
