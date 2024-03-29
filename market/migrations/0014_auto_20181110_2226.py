# Generated by Django 2.1.1 on 2018-11-10 22:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0013_auto_20181110_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(default='password', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default='user', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='itemid',
            field=models.UUIDField(default=uuid.UUID('a07c20e0-8887-4933-82c8-b1bcecebc778'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='userid',
            field=models.UUIDField(default=uuid.UUID('81a391fe-5ee6-4570-9fb6-ffe32519c1b2'), primary_key=True, serialize=False),
        ),
    ]
