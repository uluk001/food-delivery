# Generated by Django 4.0.2 on 2022-12-19 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productscart',
            name='user',
        ),
    ]
