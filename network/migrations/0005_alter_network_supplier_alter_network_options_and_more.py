# Generated by Django 5.0.7 on 2024-08-07 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_supplier_alter_network_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='network',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients', to='network.network', verbose_name='Поставщик'),
        ),
        migrations.AlterModelOptions(
            name='network',
            options={'verbose_name': 'Сеть', 'verbose_name_plural': 'Сети'},
        ),
        migrations.RemoveField(
            model_name='network',
            name='employee',
        ),
        migrations.AlterField(
            model_name='network',
            name='level',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Завод'), (1, 'Розничная сеть'), (2, 'Индивидуальный предприниматель')], editable=False, verbose_name='Уровень'),
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
    ]
