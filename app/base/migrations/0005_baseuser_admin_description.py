# Generated by Django 4.0.4 on 2022-04-28 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_baseuser_admin_stat'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='admin_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]