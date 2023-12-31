# Generated by Django 4.2.3 on 2023-08-01 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0003_alter_statistic_views_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='publication_feature',
            field=models.BooleanField(default=True, verbose_name='Признак публикации'),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='views_count',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='Количество просмотров'),
        ),
    ]
