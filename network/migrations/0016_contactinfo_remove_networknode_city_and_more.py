# Generated by Django 5.0.7 on 2024-08-09 09:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0015_remove_retailnetwork_contact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('street', models.CharField(blank=True, max_length=255, null=True)),
                ('house_number', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='networknode',
            name='city',
        ),
        migrations.RemoveField(
            model_name='networknode',
            name='country',
        ),
        migrations.RemoveField(
            model_name='networknode',
            name='email',
        ),
        migrations.RemoveField(
            model_name='networknode',
            name='house_number',
        ),
        migrations.RemoveField(
            model_name='networknode',
            name='street',
        ),
        migrations.AlterField(
            model_name='networknode',
            name='level',
            field=models.IntegerField(choices=[(0, 'Factory'), (1, 'Retail Network'), (2, 'Entrepreneur')], default=0),
        ),
        migrations.AlterField(
            model_name='networknode',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='network_nodes', to='network.product'),
        ),
        migrations.AddField(
            model_name='networknode',
            name='contact_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.contactinfo'),
        ),
    ]
