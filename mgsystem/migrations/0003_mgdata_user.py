# Generated by Django 3.2.8 on 2022-04-10 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mgsystem', '0002_mguser'),
    ]

    operations = [
        migrations.AddField(
            model_name='mgdata',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mgsystem.mguser'),
            preserve_default=False,
        ),
    ]
