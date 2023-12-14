# Generated by Django 4.2.7 on 2023-12-14 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=500)),
                ('fullname', models.CharField(max_length=500)),
                ('region', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('payment_method', models.CharField(max_length=500)),
                ('goods', models.CharField(max_length=100000)),
            ],
        )
    ]
