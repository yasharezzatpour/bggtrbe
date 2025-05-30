# Generated by Django 4.2.7 on 2024-01-02 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('context', models.TextField()),
                ('created_date_time', models.DateTimeField()),
                ('url_to_media', models.CharField(max_length=255)),
                ('video_or_image', models.BooleanField(default=False)),
                ('related_to_business_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.business')),
            ],
        ),
    ]
