# Generated by Django 4.2.3 on 2023-07-31 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='platform',
            new_name='desc',
        ),
    ]
