# Generated by Django 2.2.4 on 2021-04-01 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beat_app', '0003_auto_20201228_0110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beat',
            name='likes',
        ),
    ]
