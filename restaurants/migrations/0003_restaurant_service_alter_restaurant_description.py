# Generated by Django 4.1.4 on 2023-01-02 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_alter_restaurant_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='service',
            field=models.CharField(choices=[('Repas sur place', 'Repas sur place'), ('Vente à emporter', 'Vente à emporter'), ('Livraison', 'Livraison')], default='Repas sur place', max_length=100),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='description',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
