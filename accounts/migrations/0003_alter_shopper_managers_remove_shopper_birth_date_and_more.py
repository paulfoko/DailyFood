# Generated by Django 4.1.4 on 2023-01-13 17:35

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_shopper_birth_date_alter_shopper_phone'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='shopper',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='shopper',
            name='birth_date',
        ),
        migrations.AddField(
            model_name='shopper',
            name='date_of_birth',
            field=models.DateField(default='2002-05-17'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shopper',
            name='email',
            field=models.CharField(max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='shopper',
            name='phone',
            field=phone_field.models.PhoneField(default='680775186', help_text='Contact phone number', max_length=31),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shopper',
            name='username',
            field=models.CharField(max_length=45),
        ),
    ]