# Generated by Django 2.2 on 2021-07-22 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('sprite_url', models.CharField(max_length=200, null=True)),
                ('shiny_url', models.CharField(max_length=200, null=True)),
                ('art_url', models.CharField(max_length=200, null=True)),
                ('height', models.IntegerField(null=True)),
                ('weight', models.IntegerField(null=True)),
                ('favorited_by', models.ManyToManyField(related_name='favorites', to='login_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('rating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews_added', to='login_app.User')),
                ('likes', models.ManyToManyField(related_name='liked_reviews', to='login_app.User')),
                ('pkmn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='main_app.Pokemon')),
            ],
        ),
    ]