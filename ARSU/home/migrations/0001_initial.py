# Generated by Django 2.1.7 on 2019-05-22 17:14

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
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdf/%Y/%m/$D/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/$D/')),
                ('heading', models.CharField(blank=True, max_length=40, null=True)),
                ('text', models.TextField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='batches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('css', models.CharField(blank=True, max_length=10)),
                ('jq', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CampusNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdf/%Y/%m/$D/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/$D/')),
                ('heading', models.CharField(blank=True, max_length=40)),
                ('file', models.FileField(blank=True, null=True, upload_to='html/%Y/%m/$D/')),
                ('summary', models.TextField(blank=True, max_length=300)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/$D/')),
            ],
        ),
        migrations.CreateModel(
            name='NonAcademic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdf/%Y/%m/$D/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/$D/')),
                ('heading', models.CharField(max_length=40)),
                ('text', models.CharField(blank=True, max_length=150)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdf/%Y/%m/$D/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/$D/')),
                ('heading', models.CharField(blank=True, max_length=40, null=True)),
                ('text', models.TextField(blank=True, max_length=150)),
                ('batches', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.batches')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdf/%Y/%m/$D/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/$D/')),
                ('heading', models.CharField(blank=True, max_length=40, null=True)),
                ('text', models.TextField(blank=True, max_length=150)),
                ('batches', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.batches')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='attendance',
            name='batches',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.batches'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]