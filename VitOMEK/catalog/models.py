from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Good(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, help_text="Выберете продукт",
                                verbose_name="Продукт", null=True)
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE, help_text="Выберите Животное",
                               verbose_name="Животное", null=True, blank=True)

    price = models.DecimalField(decimal_places=2, max_digits=10, help_text="Введите цену ", verbose_name="Цена",
                                default=0)

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return '%s %s' % (self.product, self.animal)


# Продукты
class Product(models.Model):
    product_type = models.ForeignKey('TypeProduct', on_delete=models.CASCADE, help_text="Выберете тип продукта",
                                     verbose_name="Тип продукта", null=True)

    country = models.ForeignKey('Country', on_delete=models.CASCADE, help_text="Введите страну изготовителя",
                                verbose_name="Страна изготовитель", null=True)
    objects = models.Manager()

    def __str__(self):
        return '%s %s' % (self.product_type, self.country)


class TypeProduct(models.Model):
    name = models.CharField(max_length=200, help_text="Выберете тип продукта", verbose_name="Тип продукта")
    objects = models.Manager()

    def __str__(self):
        return '%s' % (self.name)


class Country(models.Model):
    name = models.CharField(max_length=200, help_text="Введите страну изготовителя", verbose_name="Страна изготовитель")
    objects = models.Manager()

    def __str__(self):
        return '%s' % (self.name)


# Животные

class Animal(models.Model):
    industry = models.ForeignKey('Industry', on_delete=models.CASCADE, help_text="Выберите Отрасль",
                                 verbose_name="Отрасль", null=True)
    animal_weight = models.ForeignKey('AnimalWeight', on_delete=models.CASCADE, help_text="Выберите вес Животного",
                                      verbose_name="Вес", null=True)
    animal_age = models.ForeignKey('Age', on_delete=models.CASCADE, help_text="Введите возраст животного",
                                   verbose_name="Возраст животного", null=True)
    objects = models.Manager()

    def __str__(self):
        return '%s %s %s' % (self.industry, self.animal_weight, self.animal_age)



class Pig(Animal):
    class Meta:
        verbose_name = "Свинья"
        verbose_name_plural = "Свиньи"


class Birds(Animal):
    animal_type = models.ForeignKey('AnimalType', on_delete=models.CASCADE, help_text="Выберите Животное",
                                    verbose_name="Животное", null=True, blank=True)

    class Meta:
        verbose_name = "Птица"
        verbose_name_plural = "Птицы"


class Cows(Animal):
    class Meta:
        verbose_name = "Корова"
        verbose_name_plural = "Коровы"


class Industry(models.Model):
    industry_animal = models.ForeignKey('TypeOfIndustry', on_delete=models.CASCADE, help_text="Выберите Отрасль",
                                        verbose_name="Отрасль", null=True)
    objects = models.Manager()

    def __str__(self):
        return '%s' % (self.industry_animal)


class TypeOfIndustry(models.Model):
    name = models.CharField(max_length=50, help_text="Введите Отрасль", verbose_name="Отрасль")
    objects = models.Manager()

    def __str__(self):
        return '%s' % (self.name)


class AnimalType(models.Model):
    name = models.CharField(max_length=200, help_text="Введите тип животного", verbose_name="Животное")
    objects = models.Manager()

    def __str__(self):
        return '%s' % (self.name)


class AnimalWeight(models.Model):
    min = models.CharField(max_length=10, help_text="Введите вес животного (от)",
                           verbose_name="Вес животного (от)", default=0)
    max = models.CharField(max_length=10, help_text="Введите вес животного (до)",
                           verbose_name="Вес животного (до)", default=0)
    objects = models.Manager()

    def __str__(self):
        return '%s %s' % (self.min, self.max)


class Age(models.Model):
    name = models.CharField(max_length=200, help_text="Введите возраст животного", verbose_name="Возраст животного")
    objects = models.Manager()

    def __str__(self):
        return '%s ' % (self.name)
