# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-08 10:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_startingbidprice'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auction', '0007_remove_auction_base_bid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='auction',
            name='product_id',
            field=models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='auction',
            name='user_bid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bid',
            name='auction_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auctions', to='auction.Auction'),
        ),
        migrations.AddField(
            model_name='bid',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
        migrations.AddField(
            model_name='bid',
            name='user_bid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.Auction'),
        ),
        migrations.AddField(
            model_name='bid',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
