# Generated by Django 2.1.2 on 2018-10-31 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20181031_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='adminid',
        ),
        migrations.RemoveField(
            model_name='item',
            name='subcateid',
        ),
        migrations.RemoveField(
            model_name='item',
            name='userid',
        ),
        migrations.AlterField(
            model_name='item',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
