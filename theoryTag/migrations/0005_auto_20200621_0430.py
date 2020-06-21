# Generated by Django 3.0.7 on 2020-06-21 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theoryTag', '0004_ques_error'),
    ]

    operations = [
        migrations.AddField(
            model_name='theory',
            name='isEasyFilled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='theory',
            name='isHardFilled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='theory',
            name='isMediumFilled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='theory',
            name='isTheoryFilled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='theory',
            name='difficulty',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
        migrations.AlterField(
            model_name='theory',
            name='importance',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
    ]
