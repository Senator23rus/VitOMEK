# Generated by Django 4.0.5 on 2022-06-30 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_good_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='maker',
            field=models.CharField(blank=True, help_text='Введите Производителя', max_length=200, null=True, verbose_name='Производитель'),
        ),
    ]