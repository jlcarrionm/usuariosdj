# Generated by Django 5.1 on 2024-09-11 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_codregistro_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='codregistro',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
