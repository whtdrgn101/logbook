# Generated by Django 3.0.3 on 2020-03-01 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scorecard', '0007_auto_20200229_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='bow',
            name='picture_type',
            field=models.CharField(max_length=25, null=True),
        ),
    ]