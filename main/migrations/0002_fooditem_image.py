# Generated by Django 3.0.4 on 2020-03-09 18:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='pics'),
            preserve_default=False,
        ),
    ]