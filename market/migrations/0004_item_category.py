# Generated by Django 2.1.1 on 2018-11-03 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20181031_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(default='Not Selected', max_length=50),
        ),
    ]
