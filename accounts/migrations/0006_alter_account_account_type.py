# Generated by Django 5.0 on 2023-12-28 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_full_name_account_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('individual', 'Individual'), ('organization', 'Organization')], default='individual', max_length=20),
        ),
    ]
