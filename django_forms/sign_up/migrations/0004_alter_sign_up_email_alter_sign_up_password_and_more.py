# Generated by Django 4.2.17 on 2024-12-15 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0003_sign_up_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign_up',
            name='email',
            field=models.EmailField(default='null@null.com', max_length=100),
        ),
        migrations.AlterField(
            model_name='sign_up',
            name='password',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='sign_up',
            name='username',
            field=models.CharField(default='null', max_length=100),
        ),
    ]