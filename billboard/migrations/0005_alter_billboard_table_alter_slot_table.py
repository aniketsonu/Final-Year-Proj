# Generated by Django 4.0.4 on 2022-04-18 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billboard', '0004_alter_slot_company'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='billboard',
            table='billboard',
        ),
        migrations.AlterModelTable(
            name='slot',
            table='slot',
        ),
    ]
