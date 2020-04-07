# Generated by Django 3.0.3 on 2020-02-26 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ManyToManyField(help_text='Select a language/s for this book', to='catalog.Language'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='catalog.Genre'),
        ),
    ]