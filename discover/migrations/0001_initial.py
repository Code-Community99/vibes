# Generated by Django 3.0.3 on 2020-03-13 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_following', models.BooleanField(default=False)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.signup')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='signup.signup')),
            ],
            options={
                'db_table': 'Followers',
            },
        ),
    ]
