# Generated by Django 3.2.8 on 2021-10-31 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Creation',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='description',
        ),
        migrations.DeleteModel(
            name='Description',
        ),
        migrations.DeleteModel(
            name='Skills',
        ),
    ]
