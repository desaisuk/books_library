# Generated by Django 2.1 on 2020-05-02 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20200502_1342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publish_date',
            new_name='publish_year',
        ),
    ]