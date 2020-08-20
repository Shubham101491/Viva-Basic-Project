# Generated by Django 2.2.10 on 2020-04-10 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='img/product')),
            ],
        ),
    ]
