# Generated by Django 2.2.14 on 2021-11-12 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rope', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='user_number',
            field=models.CharField(default=None, max_length=10,null=True, blank=True),
        ),
    ]
