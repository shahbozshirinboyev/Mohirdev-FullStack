# Generated by Django 5.2.4 on 2025-07-24 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='content',
            field=models.TextField(default=10000),
            preserve_default=False,
        ),
    ]
