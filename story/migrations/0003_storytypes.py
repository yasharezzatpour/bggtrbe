# Generated by Django 4.2.7 on 2024-01-06 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url_to_image', models.CharField(max_length=255)),
            ],
        ),
    ]
