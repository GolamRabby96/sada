# Generated by Django 2.1.2 on 2019-01-29 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20181121_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='sub_cat',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
    ]
