# Generated by Django 3.2.8 on 2022-04-12 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgsystem', '0009_alter_mgdata_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='mgdata',
            name='isdelete',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
