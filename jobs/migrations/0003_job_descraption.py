# Generated by Django 3.1.4 on 2020-12-27 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='descraption',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]