# Generated by Django 4.0 on 2021-12-08 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('czytaj', '0002_alter_author_year_of_death'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='review',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Recenzja'),
        ),
    ]
