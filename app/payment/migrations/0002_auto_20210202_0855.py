# Generated by Django 3.1.6 on 2021-02-02 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Payment',
            new_name='Transactions',
        ),
    ]