# Generated by Django 2.1.2 on 2018-11-15 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20181115_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_one',
            field=models.ImageField(upload_to='media/profile_pics'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_three',
            field=models.ImageField(blank=True, upload_to='media/profile_pics'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_two',
            field=models.ImageField(blank=True, upload_to='media/profile_pics'),
        ),
    ]
