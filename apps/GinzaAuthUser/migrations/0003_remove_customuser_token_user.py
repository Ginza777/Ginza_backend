# Generated by Django 4.2.1 on 2023-05-10 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GinzaAuthUser', '0002_alter_customuser_token_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='token_user',
        ),
    ]
