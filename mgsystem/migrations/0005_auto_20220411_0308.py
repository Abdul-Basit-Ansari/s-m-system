# Generated by Django 3.2.8 on 2022-04-10 22:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mgsystem', '0004_rename_id_mgdata_sno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mgdata',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Mguser',
        ),
    ]
