# Generated by Django 4.0 on 2021-12-15 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('czytaj', '0015_review_tittle'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='tittle',
            field=models.CharField(default='', max_length=64, verbose_name='Tytuł'),
        ),
    ]
