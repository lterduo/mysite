# Generated by Django 2.2 on 2020-12-26 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20201223_0141'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerMatched',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.CharField(max_length=64)),
                ('create_time', models.CharField(default='2020-12-26', max_length=16)),
            ],
            options={
                'verbose_name': '已匹配的头像表',
                'verbose_name_plural': '已匹配的头像表',
                'db_table': 'customer_matched',
            },
        ),
        migrations.DeleteModel(
            name='CustomerFace',
        ),
        migrations.AlterField(
            model_name='customer',
            name='relation',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
