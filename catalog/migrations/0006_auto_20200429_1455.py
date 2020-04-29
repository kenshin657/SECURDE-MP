# Generated by Django 3.0.3 on 2020-04-29 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20200407_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
        migrations.AddField(
            model_name='book',
            name='yearPub',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Book Availability', max_length=1),
        ),
    ]
