# Generated by Django 4.0 on 2022-04-09 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_messages_roompass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='roomPass',
        ),
        migrations.AddField(
            model_name='chatroom',
            name='roomPass',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
