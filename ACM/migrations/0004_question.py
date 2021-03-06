# Generated by Django 3.2.7 on 2021-09-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ACM', '0003_alter_root_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.IntegerField(auto_created=1, primary_key=True, serialize=False)),
                ('info', models.CharField(blank=True, max_length=100, null=True)),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('score', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'question',
                'managed': False,
            },
        ),
    ]
