# Generated by Django 4.1.4 on 2023-01-02 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_restaurant_image_link_alter_restaurant_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='location',
            new_name='adresse',
        ),
    ]