# Generated by Django 4.2.7 on 2023-11-07 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.TextField(),
        ),
    ]
