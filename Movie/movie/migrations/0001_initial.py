# Generated by Django 4.2.7 on 2024-01-04 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=20)),
                ('release_date', models.DateField()),
                ('duration', models.TimeField()),
                ('summary', models.CharField(max_length=600)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movie.genre')),
            ],
        ),
    ]
