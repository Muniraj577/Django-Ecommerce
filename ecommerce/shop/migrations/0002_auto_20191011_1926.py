# Generated by Django 2.2.6 on 2019-10-11 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='products',
            index_together={('id', 'name')},
        ),
    ]
