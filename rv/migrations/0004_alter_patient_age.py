# Generated by Django 5.0.6 on 2024-09-12 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rv', '0003_alter_personne_age_alter_personne_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.PositiveIntegerField(),
        ),
    ]
