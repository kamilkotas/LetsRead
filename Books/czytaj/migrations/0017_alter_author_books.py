# Generated by Django 4.0 on 2021-12-16 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('czytaj', '0016_userstory_tittle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(blank=True, to='czytaj.Book', verbose_name='Książki autora'),
        ),
    ]
