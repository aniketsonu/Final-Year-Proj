# Generated by Django 4.0.4 on 2022-04-18 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billboard',
            fields=[
                ('billboard_id', models.AutoField(primary_key=True, serialize=False)),
                ('billboard_name', models.CharField(max_length=250)),
                ('billboard_location', models.CharField(max_length=250)),
            ],
        ),
    ]