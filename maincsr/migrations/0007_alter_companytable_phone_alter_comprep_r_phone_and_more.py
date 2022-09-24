# Generated by Django 4.0.4 on 2022-08-19 15:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maincsr', '0006_rename_email_comprep_r_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companytable',
            name='phone',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator('^\\d{3}-\\d{3}-\\d{4}$')]),
        ),
        migrations.AlterField(
            model_name='comprep',
            name='r_phone',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator('^\\d{3}-\\d{3}-\\d{4}$')]),
        ),
        migrations.AlterField(
            model_name='ngorep',
            name='r_phone',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator('^\\d{3}-\\d{3}-\\d{4}$')]),
        ),
        migrations.AlterField(
            model_name='ngotable',
            name='phone',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator('^\\d{3}-\\d{3}-\\d{4}$')]),
        ),
    ]
