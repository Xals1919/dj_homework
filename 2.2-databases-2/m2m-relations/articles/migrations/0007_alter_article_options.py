# Generated by Django 4.2.7 on 2024-01-11 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_article_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
