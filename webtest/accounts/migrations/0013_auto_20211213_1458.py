# Generated by Django 3.2.7 on 2021-12-13 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
