# Generated by Django 4.0.4 on 2022-05-31 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='Book Summary'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(),
        ),
    ]
