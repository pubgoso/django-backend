# Generated by Django 3.2.7 on 2021-09-14 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ACM', '0006_submissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aclog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'AcLog',
                'managed': False,
            },
        ),
    ]
