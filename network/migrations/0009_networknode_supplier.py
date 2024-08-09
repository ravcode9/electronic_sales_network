# Generated by Django 5.0.7 on 2024-08-08 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0008_remove_product_network_networknode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='networknode',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supplied_nodes', to='network.networknode', verbose_name='Поставщик'),
        ),
    ]
