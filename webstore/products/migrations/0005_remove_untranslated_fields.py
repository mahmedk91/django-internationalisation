# Generated by Django 2.0.4 on 2018-04-23 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_migrate_translatable_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
    ]
