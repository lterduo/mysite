# Generated by Django 2.2 on 2021-01-04 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20201226_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.IntegerField()),
                ('role_name', models.CharField(max_length=16)),
            ],
            options={
                'verbose_name': '角色表',
                'verbose_name_plural': '角色表',
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('tel', models.CharField(max_length=32, null=True)),
                ('email', models.CharField(max_length=32, null=True)),
                ('addr', models.CharField(max_length=64, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('role_id', models.IntegerField()),
                ('gender', models.CharField(max_length=2, null=True)),
                ('national', models.CharField(max_length=2, null=True)),
                ('birth', models.CharField(max_length=16, null=True)),
                ('duty', models.CharField(max_length=16, null=True)),
                ('education', models.CharField(max_length=16, null=True)),
                ('origin', models.CharField(max_length=16, null=True)),
            ],
            options={
                'verbose_name': '用户信息表',
                'verbose_name_plural': '用户信息表',
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='c_id',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='waiter',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='customermatched',
            name='treated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customermatched',
            name='waiter',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='customermatched',
            name='create_time',
            field=models.CharField(default='2021-01-04', max_length=16),
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
