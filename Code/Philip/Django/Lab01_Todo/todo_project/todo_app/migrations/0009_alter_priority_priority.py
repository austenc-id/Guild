# Generated by Django 3.2.7 on 2022-01-12 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0008_alter_priority_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priority',
            name='priority',
            field=models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='low', max_length=20),
        ),
    ]
