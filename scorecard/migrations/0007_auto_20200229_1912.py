# Generated by Django 3.0.3 on 2020-03-01 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scorecard', '0006_auto_20200227_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bow',
            name='picture',
            field=models.TextField(null=True),
        ),
    ]
