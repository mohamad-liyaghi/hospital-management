# Generated by Django 4.0.4 on 2022-08-07 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospital', '0005_alter_message_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hospital_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
