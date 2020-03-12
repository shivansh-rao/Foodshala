# Generated by Django 3.0.4 on 2020-03-09 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fooditem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.CharField(max_length=100)),
                ('item', models.CharField(max_length=100)),
                ('restaurent', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
