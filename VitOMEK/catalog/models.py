from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, help_text="Введите Название Категории товара", verbose_name="Категория товара")
    objects = models.Manager()
    def __str__(self):
        return '%s' % (self.name)



class TypeOfGoods(models.Model):
    name = models.CharField(max_length=200, help_text="Введите Название типа товара", verbose_name="Тип товара")
    objects = models.Manager()

    def __str__(self):
        return '%s' % (self.name)

class Animal(models.Model):
    name = models.CharField(max_length=200, help_text="Введите вид животного", verbose_name="Животное")
    objects = models.Manager()

    def __str__(self):
        return '%s' % (self.name)

class Age(models.Model):
    name = models.CharField(max_length=200, help_text="Введите возраст животного", verbose_name="Возраст животного")
    objects = models.Manager()

    def __str__(self):
        return '%s' % (self.name)

class InputPercentage(models.Model):
    input_percentage = models.DecimalField(decimal_places=2, max_digits=4, help_text="Введите процент ввода ", verbose_name="Процент ввода", default=0)
    objects = models.Manager()

    def __str__(self):
        return '%s' % (self.input_percentage)

class Weight(models.Model):
    weight = models.DecimalField(decimal_places=2, max_digits=4, help_text="Введите вес Фасовки",
                                 verbose_name="Вес Фасовки", default=0)

    def __str__(self):
         return '%s' % (self.weight)

class Country(models.Model):
    name = models.CharField(max_length=200, help_text="Введите страну изготовителя", verbose_name="Страна изготовитель")
    objects = models.Manager()

    def __str__(self):
        return '%s' % (self.name)




class ProductPremix(models.Model):
    # salesman = models.ForeignKey(User, on_delete=models.CASCADE, related_name="salesman")
    name = models.CharField(max_length=200, help_text="Введите название Товара", verbose_name="Название Товара")
    price = models.DecimalField(decimal_places=2, max_digits=10, help_text="Введите цену ", verbose_name="Цена", default=0)
    photo = models.ImageField(default=1, upload_to='images/goods/', help_text="разместите фото", null=True)
    summary = models.TextField(max_length=1000, help_text="Введите описание", verbose_name="Описание")
    compound = models.TextField(max_length=1000, help_text="Введите состав", verbose_name="Состав")
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE, help_text="Выберите Животное", verbose_name="Животное", null=True)
    age = models.ForeignKey('Age', on_delete=models.CASCADE, help_text="Выберите возраст животного", verbose_name="Возраст", null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, help_text="Выберите категорию товара",
                               verbose_name="Категория", null=True)
    type = models.ForeignKey('TypeOfGoods', on_delete=models.CASCADE, help_text="Выберите тип товара",
                               verbose_name="Тип", null=True)
    input_percentage = models.ForeignKey('InputPercentage', on_delete=models.CASCADE, help_text="Выберите процент ввода", verbose_name="Процент ввода", null=True)
    objects = models.Manager()
    weight = models.ForeignKey('Weight', on_delete=models.CASCADE, help_text="Выберите вес товара",
                                 verbose_name="Вес", null=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, help_text="Выберите страну производитель",
                               verbose_name="Страна производитель", null=True)

    def __str__(self):
        return '%s %s %s' % (self.name, self.animal, self.price)

