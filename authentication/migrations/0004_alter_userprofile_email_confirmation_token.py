# Generated by Django 4.1.7 on 2023-11-10 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_userprofile_email_confirmation_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email_confirmation_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
