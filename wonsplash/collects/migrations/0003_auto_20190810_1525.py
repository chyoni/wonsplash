# Generated by Django 2.2.4 on 2019-08-10 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collects', '0002_auto_20190810_1243'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-created_at']},
        ),
    ]