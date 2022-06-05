# Generated by Django 4.0.5 on 2022-06-05 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=20)),
                ('phonenumber', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=254)),
                ('membertype', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=8)),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'account',
                'managed': True,
            },
        ),
    ]
