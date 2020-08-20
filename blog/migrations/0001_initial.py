# Generated by Django 2.2.10 on 2020-04-10 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('experience', models.IntegerField()),
                ('designation', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
