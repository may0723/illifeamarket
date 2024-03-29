# Generated by Django 2.1.2 on 2018-11-27 02:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0022_auto_20181126_1935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='password1',
            new_name='password',
        ),
        migrations.AlterField(
            model_name='item',
            name='itemid',
            field=models.UUIDField(default=uuid.UUID('7d6ce91d-a84a-4769-9853-0f712aa53540'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='userid',
            field=models.UUIDField(default=uuid.UUID('03323226-f38c-49a4-b85c-8ffa0c0c81ec'), primary_key=True, serialize=False),
        ),
    ]
