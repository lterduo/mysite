# Generated by Django 2.2 on 2021-02-18 23:36

from django.db import migrations, models
import django_jsonfield_backport.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0041_projectcategoryson_direction'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProjectCategorySonDirection',
        ),
        migrations.AddField(
            model_name='projectinfo',
            name='category_direction',
            field=models.CharField(help_text='课题子类方向', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='projectcategoryson',
            name='direction',
            field=django_jsonfield_backport.models.JSONField(help_text='课题方向列表', null=True),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='category',
            field=models.IntegerField(help_text='课题子类,对应project_category_son中id', null=True),
        ),
    ]
