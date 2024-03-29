# Generated by Django 2.1.1 on 2018-11-10 22:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0011_auto_20181110_2216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='username',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='item',
            name='itemid',
            field=models.UUIDField(default=uuid.UUID('482ddbd8-9e56-4965-aed5-442fa072318a'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='userid',
            field=models.UUIDField(default=uuid.UUID('ff5da7ec-0e9f-433d-8bb5-f49b73b0ed0f'), primary_key=True, serialize=False),
        ),
    ]
