# Generated by Django 4.1.4 on 2023-01-02 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_alter_restaurant_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image_link',
            field=models.CharField(blank=True, default='', max_length=7000000),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(blank=True, upload_to='restaurants'),
        ),
    ]
