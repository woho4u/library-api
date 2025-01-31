# Generated by Django 5.1.5 on 2025-01-31 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('description', models.CharField(default='This is a great book!', max_length=255)),
                ('genre', models.CharField(max_length=100)),
                ('keywords', models.JSONField(default=list, help_text='A list of keywords')),
                ('coverImage', models.URLField(help_text='Cover image link', null=True)),
                ('published_date', models.DateField()),
            ],
        ),
    ]
