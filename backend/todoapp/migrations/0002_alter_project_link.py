# Generated by Django 3.2.7 on 2021-10-20 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.CharField(blank=True, max_length=128, verbose_name='ссылка на репозиторий'),
        ),
    ]
