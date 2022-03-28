# Generated by Django 4.0.3 on 2022-03-07 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POKEDEX', '0003_species_sprite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('abilityid', models.IntegerField(primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='species',
            name='ability1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ability1', to='POKEDEX.ability'),
        ),
        migrations.AddField(
            model_name='species',
            name='ability2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ability2', to='POKEDEX.ability'),
        ),
        migrations.AddField(
            model_name='species',
            name='hidden_ability',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hidden_ability', to='POKEDEX.ability'),
        ),
    ]
