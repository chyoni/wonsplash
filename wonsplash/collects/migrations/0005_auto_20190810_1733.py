# Generated by Django 2.2.4 on 2019-08-10 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collects', '0004_auto_20190810_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.CharField(max_length=10000),
        ),
    ]