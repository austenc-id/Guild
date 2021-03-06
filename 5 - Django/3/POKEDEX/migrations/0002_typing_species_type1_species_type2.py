# Generated by Django 4.0.3 on 2022-03-07 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POKEDEX', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Typing',
            fields=[
                ('typeid', models.IntegerField(primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='species',
            name='type1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type1', to='POKEDEX.typing'),
        ),
        migrations.AddField(
            model_name='species',
            name='type2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type2', to='POKEDEX.typing'),
        ),
    ]
