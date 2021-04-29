# Generated by Django 3.1.1 on 2021-04-25 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20210423_1701'),
    ]

    operations = [
        migrations.DeleteModel(
            name='total',
        ),
        migrations.AddField(
            model_name='hospital',
            name='total_beds_with_oxygen',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='total_beds_without_oxygen',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='total_icu_with_ventilator',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='total_normal_icu',
            field=models.IntegerField(null=True),
        ),
    ]