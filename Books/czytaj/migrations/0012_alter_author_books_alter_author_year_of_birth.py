# Generated by Django 4.0 on 2021-12-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('czytaj', '0011_screenadaptation_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(null=True, to='czytaj.Book', verbose_name='Książki autora'),
        ),
        migrations.AlterField(
            model_name='author',
            name='year_of_birth',
            field=models.DateField(null=True, verbose_name='Rok urodzenia'),
        ),
    ]