# Generated by Django 4.1.2 on 2022-10-24 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_article_description_alter_article_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]