# Generated by Django 3.0.8 on 2020-07-29 13:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lancamentos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lancamentos',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lancamentos',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]