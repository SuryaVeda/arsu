# Generated by Django 2.1.7 on 2019-05-22 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=30)),
                ('img', models.ImageField(blank=True, default=None, upload_to='clubs/images/%Y/%m/$D/')),
            ],
        ),
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=30)),
                ('image', models.ImageField(default=True, null=True, upload_to='clubs/images/%Y/%m/$D/')),
                ('text', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('heading', models.CharField(max_length=30)),
                ('text', models.CharField(blank=True, max_length=80)),
                ('image', models.ImageField(blank=True, null=True, upload_to='clubs/images/%Y/%m/$D/')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clubs.Categories')),
            ],
        ),
        migrations.AddField(
            model_name='categories',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clubs.Clubs'),
        ),
    ]