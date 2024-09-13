# Generated by Django 5.0.6 on 2024-09-12 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rv', '0005_remove_rv_patient_rv_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rv',
            name='patient',
        ),
        migrations.AddField(
            model_name='rv',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rv.patient'),
            preserve_default=False,
        ),
    ]