# Generated by Django 5.0 on 2023-12-28 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_full_name_account_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='full_Name',
            new_name='full_name',
        ),
    ]
