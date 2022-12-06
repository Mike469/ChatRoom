# Generated by Django 4.1.1 on 2022-11-11 20:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_alter_channel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='user',
            field=models.ManyToManyField(blank=True, null=True, related_name='add_user', to=settings.AUTH_USER_MODEL),
        ),
    ]