# Generated by Django 4.0.4 on 2022-09-30 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maincsr', '0015_delete_certificates_ngotable_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngotable',
            name='no_of_employees',
            field=models.IntegerField(null=True),
        ),
    ]