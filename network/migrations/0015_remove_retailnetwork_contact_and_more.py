# Generated by Django 5.0.7 on 2024-08-09 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0014_contact_remove_factory_city_remove_factory_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='retailnetwork',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='individualentrepreneur',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='factory',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='product',
            name='factory',
        ),
        migrations.RemoveField(
            model_name='individualentrepreneur',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='product',
            name='individual_entrepreneur',
        ),
        migrations.RemoveField(
            model_name='retailnetwork',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='product',
            name='retail_network',
        ),
        migrations.CreateModel(
            name='NetworkNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('house_number', models.CharField(max_length=10)),
                ('debt', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('level', models.IntegerField(choices=[(0, 'Factory'), (1, 'Retail Network'), (2, 'Entrepreneur')])),
                ('products', models.ManyToManyField(related_name='network_nodes', to='network.product')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supplied_nodes', to='network.networknode')),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Factory',
        ),
        migrations.DeleteModel(
            name='IndividualEntrepreneur',
        ),
        migrations.DeleteModel(
            name='RetailNetwork',
        ),
    ]
