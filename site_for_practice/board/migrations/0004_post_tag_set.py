# Generated by Django 3.0.3 on 2020-05-07 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20200507_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag_set',
            field=models.ManyToManyField(blank=True, to='board.Tag'),
        ),
    ]
