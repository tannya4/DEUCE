# Generated by Django 2.0 on 2018-03-27 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logsign', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='sports_complex',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='team',
            field=models.ManyToManyField(to='logsign.Event'),
        ),
    ]
