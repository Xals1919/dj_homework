# Generated by Django 4.2.7 on 2024-01-11 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.ManyToManyField(related_name='scopes', to='articles.article')),
            ],
        ),
    ]