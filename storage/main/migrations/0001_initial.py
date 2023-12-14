# Generated by Django 4.2.7 on 2023-12-02 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_name', models.CharField(max_length=500, unique=True)),
                ('price', models.CharField(max_length=50)),
                ('currency', models.CharField(max_length=10)),
                ('image', models.CharField(max_length=300)),
                ('link_to_good', models.CharField(max_length=700)),
                ('info_about_good', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=500)),
                ('link_to_category', models.CharField(max_length=760)),
                ('image', models.CharField(max_length=800)),
                ('goods', models.ManyToManyField(to='main.goods')),
            ],
        ),
    ]
