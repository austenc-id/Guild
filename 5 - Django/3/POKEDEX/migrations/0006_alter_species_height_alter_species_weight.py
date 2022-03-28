# Generated by Django 4.0.3 on 2022-03-07 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POKEDEX', '0005_species_attack_species_defense_species_height_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='height',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='species',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
