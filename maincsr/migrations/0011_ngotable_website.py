# Generated by Django 4.0.4 on 2022-09-24 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maincsr', '0010_rename_state_ngotable_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngotable',
            name='website',
            field=models.CharField(max_length=156, null=True),
        ),
    ]