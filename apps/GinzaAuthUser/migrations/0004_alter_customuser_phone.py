# Generated by Django 4.2.1 on 2023-05-10 10:30

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('GinzaAuthUser', '0003_remove_customuser_token_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
