# Generated by Django 3.2 on 2023-08-18 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_proforma_condicion_pago'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultoria',
            name='tipo_moneda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.moneda'),
        ),
    ]
