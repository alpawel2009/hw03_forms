# Generated by Django 2.2.19 on 2023-01-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230122_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.TextField(max_length=100),
        ),
    ]