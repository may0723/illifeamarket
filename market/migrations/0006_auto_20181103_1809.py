# Generated by Django 2.1.1 on 2018-11-03 18:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_auto_20181103_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itemid',
            field=models.UUIDField(default=uuid.UUID('9c367e79-0783-4f30-88ea-8c2879ffdfd0'), primary_key=True, serialize=False),
        ),
    ]
