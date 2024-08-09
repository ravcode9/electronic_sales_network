# Generated by Django 5.0.7 on 2024-08-09 08:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0013_factory_individualentrepreneur_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('house_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='factory',
            name='city',
        ),
        migrations.RemoveField(
            model_name='factory',
            name='country',
        ),
        migrations.RemoveField(
            model_name='factory',
            name='email',
        ),
        migrations.RemoveField(
            model_name='factory',
            name='house_number',
        ),
        migrations.RemoveField(
            model_name='factory',
            name='street',
        ),
        migrations.RemoveField(
            model_name='individualentrepreneur',
            name='city',
        ),
        migrations.RemoveField(
            model_name='individualentrepreneur',
            name='country',
        ),
        migrations.RemoveField(
            model_name='individualentrepreneur',
            name='email',
        ),
        migrations.RemoveField(
            model_name='individualentrepreneur',
            name='house_number',
        ),
        migrations.RemoveField(
            model_name='individualentrepreneur',
            name='street',
        ),
        migrations.RemoveField(
            model_name='product',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='retailnetwork',
            name='city',
        ),
        migrations.RemoveField(
            model_name='retailnetwork',
            name='country',
        ),
        migrations.RemoveField(
            model_name='retailnetwork',
            name='email',
        ),
        migrations.RemoveField(
            model_name='retailnetwork',
            name='house_number',
        ),
        migrations.RemoveField(
            model_name='retailnetwork',
            name='street',
        ),
        migrations.AlterField(
            model_name='factory',
            name='debt',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='individualentrepreneur',
            name='debt',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='individualentrepreneur',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='individual_entrepreneurs', to='network.individualentrepreneur'),
        ),
        migrations.AlterField(
            model_name='product',
            name='factory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='network.factory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='individual_entrepreneur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='network.individualentrepreneur'),
        ),
        migrations.AlterField(
            model_name='product',
            name='model',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='retail_network',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='network.retailnetwork'),
        ),
        migrations.AlterField(
            model_name='retailnetwork',
            name='debt',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='retailnetwork',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='retail_networks', to='network.retailnetwork'),
        ),
        migrations.AddField(
            model_name='factory',
            name='contact',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.contact'),
        ),
        migrations.AddField(
            model_name='individualentrepreneur',
            name='contact',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.contact'),
        ),
        migrations.AddField(
            model_name='retailnetwork',
            name='contact',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.contact'),
        ),
    ]
