# Generated by Django 3.2.7 on 2021-09-12 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ACM', '0004_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auditlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('time_log', models.DateField()),
            ],
            options={
                'db_table': 'auditLog',
                'managed': False,
            },
        ),
    ]