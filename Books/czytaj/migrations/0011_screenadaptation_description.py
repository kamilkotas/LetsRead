# Generated by Django 4.0 on 2021-12-10 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('czytaj', '0010_alter_author_id_alter_book_id_alter_review_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='screenadaptation',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
