# Generated by Django 4.2.17 on 2024-12-15 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0007_alter_sign_up_email_alter_sign_up_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign_up',
            name='checkbox',
            field=models.BooleanField(null=True, verbose_name='Policies'),
        ),
    ]