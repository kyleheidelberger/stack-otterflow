# Generated by Django 2.2.3 on 2019-07-17 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_otter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Otter'),
        ),
        migrations.AlterField(
            model_name='question',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Otter'),
        ),
    ]
