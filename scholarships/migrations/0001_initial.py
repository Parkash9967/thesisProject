# Generated by Django 3.2.8 on 2021-11-15 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scholarships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scholarship_name', models.CharField(blank=True, max_length=100)),
                ('scholarship_url', models.CharField(blank=True, max_length=100)),
                ('scholarship_university', models.CharField(blank=True, max_length=100)),
                ('scholarship_program', models.CharField(blank=True, max_length=100)),
                ('scholarship_deadline', models.CharField(blank=True, max_length=100)),
                ('scholarship_country', models.CharField(blank=True, max_length=100)),
                ('scholarship_Start_date', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
