# Generated by Django 3.1.4 on 2020-12-14 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0002_auto_20201213_2127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='id',
            new_name='book_id',
        ),
    ]
