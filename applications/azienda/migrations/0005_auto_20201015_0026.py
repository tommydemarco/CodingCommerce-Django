# Generated by Django 3.1.1 on 2020-10-14 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azienda', '0004_auto_20201015_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='fb_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='ig_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='tw_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
