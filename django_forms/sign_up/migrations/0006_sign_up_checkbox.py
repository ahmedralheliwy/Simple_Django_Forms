# Generated by Django 4.2.17 on 2024-12-15 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0005_alter_sign_up_password_alter_sign_up_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='sign_up',
            name='checkbox',
            field=models.BooleanField(default=True, verbose_name='Policies'),
        ),
    ]
