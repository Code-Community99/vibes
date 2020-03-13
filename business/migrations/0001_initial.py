# Generated by Django 3.0.3 on 2020-03-11 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sell_goods',
            fields=[
                ('GoodId', models.AutoField(primary_key=True, serialize=False)),
                ('Gtitle', models.CharField(max_length=255)),
                ('GDescription', models.CharField(max_length=255)),
                ('GLocation', models.CharField(default='Narobi/Kenya', max_length=255)),
                ('Gprice', models.FloatField(max_length=10)),
                ('Gphoto', models.FileField(upload_to='')),
                ('Sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_id', to='signup.signup')),
            ],
            options={
                'db_table': 'Goods',
            },
        ),
    ]
