# Generated by Django 4.0 on 2021-12-08 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('czytaj', '0004_remove_book_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='book_author',
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='czytaj.book', verbose_name='Książki'),
        ),
    ]
