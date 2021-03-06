# Generated by Django 2.2 on 2020-10-27 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('organization', models.CharField(max_length=32)),
                ('tel', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
                ('addr', models.CharField(max_length=64)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '申报人信息表',
                'verbose_name_plural': '申报人信息表',
                'db_table': 'applicant',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('organization', models.CharField(max_length=32)),
                ('tel', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
                ('addr', models.CharField(max_length=64)),
                ('is_active', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('role_id', models.IntegerField()),
            ],
            options={
                'verbose_name': '用户信息表',
                'verbose_name_plural': '用户信息表',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=60)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='api.User')),
            ],
            options={
                'verbose_name': '用户token表',
                'verbose_name_plural': '用户token表',
                'db_table': 'user_token',
            },
        ),
    ]
