# Generated by Django 3.0.5 on 2020-05-03 15:23

import django.db.models.deletion

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("accounts", "0003_auto_20200420_1720")]

    operations = [
        migrations.AlterField(
            model_name="family",
            name="creator",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created_families",
                to=settings.AUTH_USER_MODEL,
            ),
        )
    ]