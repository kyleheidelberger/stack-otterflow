# Generated by Django 2.2.3 on 2019-07-17 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190717_1530'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='otterprofile',
            options={'ordering': ['user', 'bio']},
        ),
        migrations.RenameField(
            model_name='otterprofile',
            old_name='username',
            new_name='user',
        ),
    ]
