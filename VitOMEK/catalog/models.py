from django.db import models
from django.urls import reverse

class TypeOfGoods(models.Model):
    name = models.CharField(max_length=200, help_text="Введите тип Продуктовой линейки", verbose_name="Продуктовая линейка")
    def __str__(self):
        return self.name

class TypeOfPremix(models.Model):
    name = models.CharField(max_length=200, help_text="Введите тип Премикса", verbose_name="Тип Премикса")
    def __str__(self):
        return self.name

class TypeOfBlands(models.Model):
    name = models.CharField(max_length=200, help_text="Введите тип Бленда", verbose_name="Тип Бленда")
    def __str__(self):
        return self.name

class TypeOfMaterials(models.Model):
    name = models.CharField(max_length=200, help_text="Введите тип Сырья", verbose_name="Тип Сырья")
    def __str__(self):
        return self.name

class TypeOfPackaging(models.Model):
    name = models.CharField(max_length=200, help_text="Введите тип Фасовки", verbose_name="Тип Фасовки")
    def __str__(self):
        return self.name

class TypeOfPremixForBroiler(models.Model):
    name = models.CharField(max_length=200, help_text="Введите тип Премикса для Бройлера", verbose_name="Тип Премикса Бройлер")
    def __str__(self):
        return self.name


class TypeOfPremixForPigs(models.Model):
    name = models.CharField(max_length=200, help_text="Введите тип Премикса для Свиней",
                            verbose_name="Тип Премикса Свиньи")

    def __str__(self):
        return self.name

class TypeOfPremixForPiglets(models.Model):
    name = models.CharField(max_length=200, help_text="Введите тип Премикса для Поросят",
                            verbose_name="Тип Премикса Поросята")

    def __str__(self):
        return self.name


class Materials(models.Model):
    name = models.CharField(max_length=200, help_text="Введите название сырья", verbose_name="Название сырья")
    type = models.ForeignKey('TypeOfMaterials', on_delete=models.CASCADE, help_text="Выбрать тип сырья", verbose_name="тип сырья", null=True)
    type_of_goods = models.ForeignKey('TypeOfGoods', on_delete=models.CASCADE, help_text="Выбрать тип продукта", verbose_name="Тип продукта", null=True)
    type_of_packing = models.ForeignKey('TypeOfPackaging', on_delete=models.CASCADE, help_text="Выбрать тип фасовки", verbose_name="Тип фасовки", null=True)
    photo = models.ImageField(default=1, upload_to='images/materials/', help_text="разместите фото")
    summary = models.TextField(max_length=1000, help_text="Введите описание сырья", verbose_name="Описание сырья")
    price = models.CharField(max_length=100, help_text="Введите цену", verbose_name="Цена")
    objects = models.Manager()

class Blands(models.Model):
    name = models.CharField(max_length=200, help_text="Введите название бленда", verbose_name="Название бленда")
    type = models.ForeignKey('TypeOfBlands', on_delete=models.CASCADE, help_text="Выбрать тип бленда", verbose_name="тип бленда", null=True)
    type_of_goods = models.ForeignKey('TypeOfGoods', on_delete=models.CASCADE, help_text="Выбрать тип продукта", verbose_name="Тип продукта", null=True)
    type_of_packing = models.ForeignKey('TypeOfPackaging', on_delete=models.CASCADE, help_text="Выбрать тип фасовки", verbose_name="Тип фасовки", null=True)
    photo = models.ImageField(default=1, upload_to='images/blands/', help_text="разместите фото")
    summary = models.TextField(max_length=1000, help_text="Введите описание бленда", verbose_name="Описание бленда")
    price = models.CharField(max_length=100, help_text="Введите цену", verbose_name="Цена")
    objects = models.Manager()

class PremixForBroiler(models.Model):
    name = models.CharField(max_length=200, help_text="Введите название премикса для Бройлеров", verbose_name="Название премикса для Бройлеров")
    type_of_premix = models.ForeignKey('TypeOfPremix', on_delete=models.CASCADE, help_text="Выбрать тип премикса", verbose_name="тип премикса", null=True)
    type = models.ForeignKey('TypeOfPremixForBroiler', on_delete=models.CASCADE, help_text="Выбрать тип премикса для Бройлеров", verbose_name="тип премикса для Бройлеров", null=True)
    type_of_goods = models.ForeignKey('TypeOfGoods', on_delete=models.CASCADE, help_text="Выбрать тип продукта", verbose_name="Тип продукта", null=True)
    type_of_packing = models.ForeignKey('TypeOfPackaging', on_delete=models.CASCADE, help_text="Выбрать тип фасовки", verbose_name="Тип фасовки", null=True)
    photo = models.ImageField(default=1, upload_to='images/premix/', help_text="разместите фото")
    summary = models.TextField(max_length=1000, help_text="Введите описание премикса", verbose_name="Описание премикса")
    price = models.CharField(max_length=100, help_text="Введите цену", verbose_name="Цена")
    objects = models.Manager()

class PremixForPig(models.Model):
    name = models.CharField(max_length=200, help_text="Введите название премикса для Свиней", verbose_name="Название премикса для Свиней")
    type_of_premix = models.ForeignKey('TypeOfPremix', on_delete=models.CASCADE, help_text="Выбрать тип премикса", verbose_name="тип премикса", null=True)
    type_premix_for_pigs = models.ForeignKey('TypeOfPremixForPigs', on_delete=models.CASCADE, help_text="Выбрать тип премикса для Свиней", verbose_name="тип премикса для Свиней", null=True)
    type_of_goods = models.ForeignKey('TypeOfGoods', on_delete=models.CASCADE, help_text="Выбрать тип продукта", verbose_name="Тип продукта", null=True)
    type_of_packing = models.ForeignKey('TypeOfPackaging', on_delete=models.CASCADE, help_text="Выбрать тип фасовки", verbose_name="Тип фасовки", null=True)
    photo = models.ImageField(default=1, upload_to='images/premix/', help_text="разместите фото")
    summary = models.TextField(max_length=1000, help_text="Введите описание премикса", verbose_name="Описание премикса")
    price = models.CharField(max_length=100, help_text="Введите цену", verbose_name="Цена")
    objects = models.Manager()

class PremixForPiglets(models.Model):
    name = models.CharField(max_length=200, help_text="Введите название премикса для Поросят", verbose_name="Название премикса для Поросят")
    type_of_premix = models.ForeignKey('TypeOfPremix', on_delete=models.CASCADE, help_text="Выбрать тип премикса", verbose_name="тип премикса", null=True)
    type_premix_for_piglets = models.ForeignKey('TypeOfPremixForPiglets', on_delete=models.CASCADE, help_text="Выбрать тип премикса для Поросят", verbose_name="тип премикса для Поросят", null=True)
    type_of_goods = models.ForeignKey('TypeOfGoods', on_delete=models.CASCADE, help_text="Выбрать тип продукта", verbose_name="Тип продукта", null=True)
    type_of_packing = models.ForeignKey('TypeOfPackaging', on_delete=models.CASCADE, help_text="Выбрать тип фасовки", verbose_name="Тип фасовки", null=True)
    photo = models.ImageField(default=1, upload_to='images/premix/', help_text="разместите фото")
    summary = models.TextField(max_length=1000, help_text="Введите описание премикса", verbose_name="Описание премикса")
    price = models.CharField(max_length=100, help_text="Введите цену", verbose_name="Цена")
    objects = models.Manager()

class PremixForCows(models.Model):
    name = models.CharField(max_length=200, help_text="Введите название премикса для KPC", verbose_name="Название премикса для KPC")
    type_of_premix = models.ForeignKey('TypeOfPremix', on_delete=models.CASCADE, help_text="Выбрать тип премикса", verbose_name="тип премикса", null=True)
    type_of_goods = models.ForeignKey('TypeOfGoods', on_delete=models.CASCADE, help_text="Выбрать тип продукта", verbose_name="Тип продукта", null=True)
    type_of_packing = models.ForeignKey('TypeOfPackaging', on_delete=models.CASCADE, help_text="Выбрать тип фасовки", verbose_name="Тип фасовки", null=True)
    photo = models.ImageField(default=1, upload_to='images/premix/', help_text="разместите фото")
    summary = models.TextField(max_length=1000, help_text="Введите описание премикса", verbose_name="Описание премикса")
    price = models.CharField(max_length=100, help_text="Введите цену", verbose_name="Цена")
    objects = models.Manager()