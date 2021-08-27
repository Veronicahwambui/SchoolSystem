# Generated by Django 3.2.4 on 2021-08-20 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.PositiveSmallIntegerField()),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=18)),
                ('student_id', models.CharField(max_length=16)),
                ('class_name', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('F', 'female'), ('m', 'male'), ('o', 'other')], max_length=10)),
                ('nationality', models.CharField(choices=[('E', 'Rwanda'), ('K', 'Kenya'), ('U', 'Uganda')], max_length=15)),
                ('city', models.CharField(max_length=12)),
                ('admission_date', models.DateField(null=True)),
                ('guardian_name', models.CharField(max_length=15)),
                ('guardian_phone_number', models.CharField(max_length=18)),
                ('academic_year', models.BigIntegerField(blank=True, null=True)),
                ('profile_pic', models.ImageField(default=None, upload_to='Images')),
                ('medical_report', models.FileField(default=None, upload_to='files')),
            ],
        ),
    ]
