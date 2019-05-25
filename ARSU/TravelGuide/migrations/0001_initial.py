# Generated by Django 2.1.7 on 2019-05-22 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='travel/images/%Y/%m/$D/')),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(default='fuck', max_length=20)),
                ('itinerary', models.CharField(blank=True, max_length=1000, null=True)),
                ('budget', models.CharField(blank=True, max_length=200, null=True)),
                ('experience', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.ImageField(default=None, upload_to='travel/images/%Y/%m/$D/')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='images',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='TravelGuide.Travel'),
        ),
    ]