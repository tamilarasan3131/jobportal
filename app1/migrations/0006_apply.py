# Generated by Django 5.0 on 2023-12-15 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(null=True, upload_to='')),
                ('applydate', models.DateField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.job')),
                ('jsuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.jobskrsignup')),
            ],
        ),
    ]
