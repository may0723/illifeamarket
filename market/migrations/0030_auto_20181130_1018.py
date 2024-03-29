# Generated by Django 2.1.3 on 2018-11-30 16:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0029_auto_20181130_0619'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Confirmation Code',
                'verbose_name_plural': 'Confirmation Code',
                'ordering': ['-c_time'],
            },
        ),
        migrations.AddField(
            model_name='userprofile',
            name='has_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='itemid',
            field=models.UUIDField(default=uuid.UUID('fa076c24-cabf-4db5-bd45-f9a9b8045b44'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='userid',
            field=models.UUIDField(default=uuid.UUID('52e8d11c-cbb0-441d-8228-20ad6d638430'), primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='confirmstring',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='market.UserProfile'),
        ),
    ]
