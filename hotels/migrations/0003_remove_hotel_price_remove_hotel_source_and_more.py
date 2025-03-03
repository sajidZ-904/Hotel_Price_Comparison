# Generated by Django 4.2.18 on 2025-02-02 06:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotels', '0002_hotel_bookmarked_by_alter_hotel_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='price',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='source',
        ),
        migrations.AddField(
            model_name='hotel',
            name='agoda_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='price_agoda',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='price_booking',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='booking_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='bookmarked_by',
            field=models.ManyToManyField(blank=True, related_name='bookmarked_hotels', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='star_rating',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
        migrations.DeleteModel(
            name='Bookmark',
        ),
    ]
