# Generated by Django 2.0 on 2018-03-27 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logsign', '0004_auto_20180327_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='owner',
        ),
        migrations.AddField(
            model_name='event',
            name='username',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]