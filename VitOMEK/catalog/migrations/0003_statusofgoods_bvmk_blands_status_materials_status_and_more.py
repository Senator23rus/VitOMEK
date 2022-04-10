# Generated by Django 4.0.3 on 2022-04-10 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_typeofpremixforbroiler_typeofpremixforpiglets_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusOfGoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите статус товара', max_length=20, verbose_name='Статус товара')),
            ],
        ),
        migrations.CreateModel(
            name='bvmk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название БВМК', max_length=200, verbose_name='Название БВМК')),
                ('photo', models.ImageField(default=1, help_text='разместите фото', upload_to='images/premix/')),
                ('summary', models.TextField(help_text='Введите описание ', max_length=1000, verbose_name='Описание')),
                ('price', models.CharField(help_text='Введите цену', max_length=100, verbose_name='Цена')),
                ('status', models.ForeignKey(help_text='Выбрать статус', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.statusofgoods', verbose_name='Статус')),
                ('type_of_goods', models.ForeignKey(help_text='Выбрать тип продукта', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.typeofgoods', verbose_name='Тип продукта')),
                ('type_of_packing', models.ForeignKey(help_text='Выбрать тип фасовки', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.typeofpackaging', verbose_name='Тип фасовки')),
            ],
        ),
        migrations.AddField(
            model_name='blands',
            name='status',
            field=models.ForeignKey(help_text='Выбрать статус', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.statusofgoods', verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='materials',
            name='status',
            field=models.ForeignKey(help_text='Выбрать статус', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.statusofgoods', verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='premixforbroiler',
            name='status',
            field=models.ForeignKey(help_text='Выбрать статус', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.statusofgoods', verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='premixforcows',
            name='status',
            field=models.ForeignKey(help_text='Выбрать статус', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.statusofgoods', verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='premixforpig',
            name='status',
            field=models.ForeignKey(help_text='Выбрать статус', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.statusofgoods', verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='premixforpiglets',
            name='status',
            field=models.ForeignKey(help_text='Выбрать статус', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.statusofgoods', verbose_name='Статус'),
        ),
    ]
