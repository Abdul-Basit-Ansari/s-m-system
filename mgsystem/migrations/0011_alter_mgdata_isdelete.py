# Generated by Django 3.2.8 on 2022-04-12 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgsystem', '0010_mgdata_isdelete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mgdata',
            name='isdelete',
            field=models.BooleanField(default=False),
        ),
    ]
