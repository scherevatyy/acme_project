# Generated by Django 3.2.16 on 2023-05-14 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('birthday', '0002_auto_20230513_0817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='birthday',
            name='image',
        ),
        migrations.AddField(
            model_name='birthday',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор записи'),
        ),
    ]
