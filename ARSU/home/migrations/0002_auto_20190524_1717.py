# Generated by Django 2.2.1 on 2019-05-24 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='heading',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='results',
            name='heading',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='heading',
            field=models.CharField(max_length=40, null=True),
        ),
    ]