# Generated by Django 4.0.6 on 2022-07-26 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tag_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='descriptions',
            field=models.TextField(blank=True, null=True, unique=True),
        ),
    ]
