# Generated by Django 3.2.4 on 2021-09-10 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Root',
            fields=[
                ('id', models.IntegerField(auto_created=1, primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('passWord', models.CharField(max_length=20)),
            ],
        ),
    ]
