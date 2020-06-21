# Generated by Django 3.0.7 on 2020-06-18 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_delete_ck'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_teacher',
        ),
        migrations.AddField(
            model_name='user',
            name='can_add_cross',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='can_add_tag',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='can_add_theory',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='can_see_cross',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='can_see_tag',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='can_see_theory',
            field=models.BooleanField(default=True),
        ),
    ]