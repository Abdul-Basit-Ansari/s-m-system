# Generated by Django 3.2.8 on 2022-04-11 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgsystem', '0005_auto_20220411_0308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('rep', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='mgdata',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='mgdata',
            name='disease',
        ),
        migrations.AddField(
            model_name='mgdata',
            name='email',
            field=models.EmailField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mgdata',
            name='img',
            field=models.ImageField(default=1, upload_to='media/studentsimg/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mgdata',
            name='section',
            field=models.CharField(default='', max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='mgdata',
            name='stuclass',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
