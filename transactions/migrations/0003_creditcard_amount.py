# Generated by Django 4.2.5 on 2023-10-16 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_creditcard'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
