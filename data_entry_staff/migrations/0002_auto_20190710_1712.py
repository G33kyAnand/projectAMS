# Generated by Django 2.1.4 on 2019-07-10 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry_staff', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Credential',
            new_name='DES_Credential',
        ),
    ]