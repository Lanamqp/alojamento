# Generated by Django 5.0.3 on 2024-09-26 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quarto',
            name='pessoas',
        ),
        migrations.AddField(
            model_name='quarto',
            name='pessoas',
            field=models.ManyToManyField(related_name='quartos', to='app.pessoa'),
        ),
    ]
