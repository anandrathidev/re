# Generated by Django 2.0 on 2019-05-21 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_auto_20190521_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregister',
            name='phone_number',
            field=models.CharField(help_text='Starts with +910', max_length=20),
        ),
    ]