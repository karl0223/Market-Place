# Generated by Django 5.0 on 2023-12-11 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_rename_items_item_alter_item_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='item/images'),
        ),
    ]