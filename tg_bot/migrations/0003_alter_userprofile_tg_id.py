# Generated by Django 4.2 on 2023-04-23 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg_bot', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='tg_id',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Telegram ID пользователя'),
        ),
    ]
