# Generated by Django 3.2.8 on 2021-12-20 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Top10',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('url', models.CharField(blank=True, max_length=100)),
                ('university', models.CharField(blank=True, max_length=100)),
                ('program', models.CharField(blank=True, max_length=100)),
                ('scholarship_country', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]