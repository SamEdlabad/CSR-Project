# Generated by Django 4.0.4 on 2022-10-02 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maincsr', '0017_alter_ngotable_min_cap_reqd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngotable',
            name='pdf',
            field=models.FileField(upload_to=''),
        ),
    ]
