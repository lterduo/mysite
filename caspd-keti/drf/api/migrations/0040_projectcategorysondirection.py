# Generated by Django 2.2 on 2021-02-16 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_remove_projectcategoryson_directions'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCategorySonDirection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(help_text='类别名，对应父类', max_length=32)),
                ('name', models.CharField(help_text='方向名', max_length=32)),
                ('desc', models.CharField(max_length=64, null=True)),
            ],
            options={
                'verbose_name': '课题类别子类方向表',
                'verbose_name_plural': '课题类别子类方向表',
                'db_table': 'project_category_son_direction',
            },
        ),
    ]
