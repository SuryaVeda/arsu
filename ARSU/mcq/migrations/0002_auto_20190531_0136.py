# Generated by Django 2.2.1 on 2019-05-30 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fact',
            name='answer',
            field=models.CharField(max_length=540),
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='answer',
            field=models.CharField(max_length=540),
        ),
    ]
