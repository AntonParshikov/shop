# Generated by Django 4.2.3 on 2023-07-20 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0002_statistic_content_statistic_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='views_count',
            field=models.IntegerField(default=0, verbose_name='Количество просмотров'),
        ),
    ]
