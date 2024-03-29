# Generated by Django 3.2.4 on 2021-09-26 09:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=17, null=True)),
                ('description', models.CharField(blank=True, max_length=60, null=True)),
                ('date_of_event', models.DateField()),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('duration', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
