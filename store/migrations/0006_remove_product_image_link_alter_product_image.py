# Generated by Django 4.1.4 on 2022-12-19 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_image_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_link',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products'),
        ),
    ]
