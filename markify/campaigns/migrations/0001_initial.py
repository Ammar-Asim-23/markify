# Generated by Django 4.2.5 on 2023-10-05 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0006_remove_client_team'),
        ('product', '0003_advertisement_activity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaigns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('ads', models.ManyToManyField(related_name='campaigns', to='product.advertisement')),
                ('clients', models.ManyToManyField(related_name='campaigns', to='client.client')),
            ],
        ),
    ]
