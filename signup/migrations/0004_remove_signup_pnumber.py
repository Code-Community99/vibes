# Generated by Django 3.0.6 on 2020-06-14 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_auto_20200602_0538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='pnumber',
        ),
    ]