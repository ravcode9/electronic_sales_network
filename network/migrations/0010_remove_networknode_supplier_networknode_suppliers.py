# Generated by Django 5.0.7 on 2024-08-09 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_networknode_supplier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='networknode',
            name='supplier',
        ),
        migrations.AddField(
            model_name='networknode',
            name='suppliers',
            field=models.ManyToManyField(blank=True, related_name='clients', to='network.networknode', verbose_name='Поставщики'),
        ),
    ]
