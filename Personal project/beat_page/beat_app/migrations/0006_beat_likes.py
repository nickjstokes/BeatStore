# Generated by Django 2.2.4 on 2021-04-03 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beat_app', '0005_auto_20210401_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='beat',
            name='likes',
            field=models.ManyToManyField(related_name='liked_beats', to='beat_app.User'),
        ),
    ]