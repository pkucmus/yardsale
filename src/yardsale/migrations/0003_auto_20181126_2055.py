# Generated by Django 2.1.3 on 2018-11-26 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yardsale', '0002_auto_20181125_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='state',
            field=models.CharField(choices=[('NEW', 'NEW'), ('PREPARED', 'PREPARED'), ('PROCESSED', 'PROCESSED'), ('INVALIDATED', 'INVALIDATED')], max_length=255),
        ),
    ]