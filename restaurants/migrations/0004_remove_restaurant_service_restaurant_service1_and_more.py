# Generated by Django 4.1.4 on 2023-01-02 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_restaurant_service_alter_restaurant_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='service',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='service1',
            field=models.CharField(blank=True, choices=[('Vente à emporter', 'Vente à emporter'), ('Livraison', 'Livraison')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='service2',
            field=models.CharField(blank=True, choices=[('Vente à emporter', 'Vente à emporter'), ('Livraison', 'Livraison')], max_length=50, null=True),
        ),
    ]
