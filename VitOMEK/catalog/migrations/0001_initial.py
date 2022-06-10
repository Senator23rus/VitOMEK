# Generated by Django 3.0.9 on 2022-06-09 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите возраст животного', max_length=200, verbose_name='Возраст животного')),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите вид животного', max_length=200, verbose_name='Животное')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите Название Категории товара', max_length=200, verbose_name='Категория товара')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите страну изготовителя', max_length=200, verbose_name='Страна изготовитель')),
            ],
        ),
        migrations.CreateModel(
            name='InputPercentage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_percentage', models.DecimalField(decimal_places=2, default=0, help_text='Введите процент ввода ', max_digits=2, verbose_name='Процент ввода')),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите Название типа товара', max_length=200, verbose_name='Тип товара')),
            ],
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=2, default=0, help_text='Введите вес Фасовки', max_digits=2, verbose_name='Вес Фасовки')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название Товара', max_length=200, verbose_name='Название Товара')),
                ('price', models.DecimalField(decimal_places=2, default=0, help_text='Введите цену ', max_digits=2, verbose_name='Цена')),
                ('photo', models.ImageField(default=1, help_text='разместите фото', null=True, upload_to='images/goods/')),
                ('summary', models.TextField(help_text='Введите описание', max_length=1000, verbose_name='Описание')),
                ('compound', models.TextField(help_text='Введите состав', max_length=1000, verbose_name='Состав')),
                ('age', models.ForeignKey(help_text='Выберите возраст животного', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Age', verbose_name='Возраст')),
                ('animal', models.ForeignKey(help_text='Выберите Животное', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Animal', verbose_name='Животное')),
                ('category', models.ForeignKey(help_text='Выберите категорию товара', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Category', verbose_name='Категория')),
                ('input_percentage', models.ForeignKey(help_text='Выберите процент ввода', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.InputPercentage', verbose_name='Процент ввода')),
                ('type', models.ForeignKey(help_text='Выберите тип товара', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.TypeOfGoods', verbose_name='Тип')),
            ],
        ),
    ]