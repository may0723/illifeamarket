# Generated by Django 2.1.2 on 2018-11-30 06:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0028_auto_20181130_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itemid',
            field=models.UUIDField(default=uuid.UUID('8d82bdad-62b7-48b1-af4a-6e0412114ffb'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='userid',
            field=models.UUIDField(default=uuid.UUID('5ed423dc-5c32-4ba6-8a91-98a70412f2f5'), primary_key=True, serialize=False),
        ),
    ]
