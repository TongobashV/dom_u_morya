# Generated by Django 5.0.6 on 2024-06-08 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_alter_house_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house',
            options={'ordering': ['name'], 'verbose_name': 'дом', 'verbose_name_plural': 'дома'},
        ),
        migrations.AddField(
            model_name='house',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='houses/photo', verbose_name='фотография'),
        ),
    ]
