# Generated by Django 4.1.7 on 2023-11-10 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email_confirmation_token',
            field=models.CharField(default='', max_length=100),
        ),
    ]
