# Generated by Django 2.2 on 2021-07-08 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0004_auto_20210707_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='default_img',
            field=models.CharField(default=0, max_length=2),
        ),
    ]
