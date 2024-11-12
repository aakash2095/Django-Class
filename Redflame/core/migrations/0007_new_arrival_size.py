# Generated by Django 5.1.1 on 2024-11-12 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_cartupperwear_product_new_arrival_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='new_arrival',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], default='S', max_length=2),
        ),
    ]