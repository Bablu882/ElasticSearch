# Generated by Django 4.1.4 on 2022-12-30 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_delete_allfielddata_delete_interestjunction'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Junction',
            new_name='InterestJunction',
        ),
    ]
