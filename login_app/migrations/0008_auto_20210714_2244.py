# Generated by Django 2.2 on 2021-07-15 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0007_auto_20210714_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followers',
        ),
        migrations.CreateModel(
            name='Follows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='login_app.User')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='login_app.User')),
            ],
        ),
    ]