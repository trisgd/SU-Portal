# Generated by Django 2.0 on 2018-02-03 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180131_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('complaint_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('complaint', models.TextField(max_length=3000)),
                ('uploadedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='complaint-logger')),
            ],
            options={
                'verbose_name': 'complaints',
                'ordering': ['complaint_id'],
            },
        ),
    ]
