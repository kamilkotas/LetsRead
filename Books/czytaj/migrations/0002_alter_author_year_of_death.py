# Generated by Django 4.0 on 2021-12-08 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('czytaj', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='year_of_death',
            field=models.DateField(blank=True, default=None, help_text='opcjonalnie: jeżeli nie żyje', null=True, verbose_name='Rok śmierci'),
        ),
    ]