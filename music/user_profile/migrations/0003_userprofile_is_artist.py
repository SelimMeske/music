# Generated by Django 3.1.7 on 2021-03-02 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20210302_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_artist',
            field=models.BooleanField(default=False),
        ),
    ]
