# Generated by Django 3.1.4 on 2020-12-14 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0004_auto_20201214_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]