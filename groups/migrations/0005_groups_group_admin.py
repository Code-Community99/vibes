# Generated by Django 3.0.3 on 2020-03-12 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
        ('groups', '0004_auto_20200311_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='group_admin',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='signup.signup'),
            preserve_default=False,
        ),
    ]
