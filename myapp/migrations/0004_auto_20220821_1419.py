# Generated by Django 3.0 on 2022-08-21 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20220821_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='uom_id',
            field=models.IntegerField(null=True),
        ),
    ]
