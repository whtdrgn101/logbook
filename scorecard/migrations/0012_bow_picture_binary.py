# Generated by Django 3.0.3 on 2020-07-22 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scorecard', '0011_auto_20200305_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='bow',
            name='picture_binary',
            field=models.BinaryField(null=True),
        ),
    ]
