# Generated by Django 4.0.4 on 2022-09-24 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maincsr', '0007_ngotable_regis_num_ngotable_sectors_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngotable',
            name='sectors',
            field=models.TextField(max_length=512, null=True),
        ),
    ]
