# Generated by Django 3.1.1 on 2021-04-25 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0005_auto_20210425_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
