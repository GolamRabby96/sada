# Generated by Django 2.1.2 on 2018-11-18 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20181117_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
