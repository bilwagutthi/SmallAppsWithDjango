# Generated by Django 3.1.6 on 2021-02-08 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shortner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('link', models.CharField(max_length=10000, primary_key=True, serialize=False)),
                ('uuid', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Urls',
        ),
    ]
