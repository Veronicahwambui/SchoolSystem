# Generated by Django 3.2.4 on 2021-08-29 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=25)),
                ('trainer', models.CharField(max_length=19)),
                ('course_code', models.IntegerField()),
                ('description', models.TextField(max_length=70)),
            ],
        ),
    ]
