# Generated by Django 3.2 on 2021-04-25 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='summary',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
