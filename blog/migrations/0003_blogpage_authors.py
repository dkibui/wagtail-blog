# Generated by Django 4.2.4 on 2023-09-03 07:39

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='authors',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='blog.author'),
        ),
    ]
