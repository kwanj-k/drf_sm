# Generated by Django 2.2.9 on 2021-01-09 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stores', '0002_auto_20200214_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='stocks', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
