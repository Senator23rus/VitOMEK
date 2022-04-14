from django.db import models
from django.urls import reverse

class TypeOfGoods(models.Model):
    name = models.CharField(max_length=200, help_text="Введите Название Категории товара", verbose_name="Категория товара")
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE, help_text="Выбрать Животное", verbose_name="Животное", null=True)
    material = models.ForeignKey('TypeOfMaterials', on_delete=models.CASCADE, help_text="Выбрать Сырьё", verbose_name="Сырьё", null=True)
    objects = models.Manager()

    def __str__(self):
        return '%s %s %s' % (self.name, self.animal, self.material)

class TypeOfMaterials(models.Model):
    name = models.CharField(max_length=200, help_text="Введите тип Сырья", verbose_name="Тип Сырья")
    packaging = models.ForeignKey('TypeOfPackaging', on_delete=models.CASCADE, help_text="Выбрать Фасовку", verbose_name="Фасовка", null=True)
    objects = models.Manager()

    def __str__(self):
        return '%s %s' % (self.name, self.packaging)

class TypeOfPackaging(models.Model):
    name = models.CharField(max_length=200, help_text="Введите название Фасовки", verbose_name="Фасовка")
    type = models.CharField(max_length=200, help_text="Введите тип Фасовки", verbose_name="Тип Фасовки", default=1)
    material = models.CharField(max_length=200, help_text="Введите материал Фасовки", verbose_name="Материал Фасовки", default=0)
    weight = models.DecimalField(decimal_places=2, max_digits=2, help_text="Введите вес Фасовки", verbose_name="Вес Фасовки", default=0)
    objects = models.Manager()

    def __str__(self):
        return '%s %s %s %s' % (self.name, self.type, self.material, self.weight)


class StatusOfGoods(models.Model):
    name = models.CharField(max_length=20, help_text="Введите статус товара", verbose_name="Статус товара")
    objects = models.Manager()
    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=200, help_text="Введите вид животного", verbose_name="Животное")
    age = models.CharField(max_length=10, help_text="Введите возраст животного", verbose_name="Возраст")
    life_stage = models.CharField(max_length=200, help_text="Введите жизненный период животного", verbose_name="Период Животного", null=True)
    weight_animal = models.DecimalField(decimal_places=2, max_digits=2, help_text="Введите вес Животного", verbose_name="Вес Животного", null=True)
    objects = models.Manager()

    def __str__(self):
        return '%s %s %s %s' % (self.name, self.age, self.life_stage, self.weight_animal)

class Goods(models.Model):
    name = models.CharField(max_length=200, help_text="Введите название Товара", verbose_name="Название Товара")
    packaging = models.ForeignKey('TypeOfPackaging', on_delete=models.CASCADE, help_text="Выбрать Фасовку", verbose_name="Фасовка", null=True)
    price = models.CharField(max_length=100, help_text="Введите цену", verbose_name="Цена")
    photo = models.ImageField(default=1, upload_to='images/goods/', help_text="разместите фото", null=True)
    summary = models.TextField(max_length=1000, help_text="Введите описание бленда", verbose_name="Описание бленда")
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE, help_text="Выберите Животное", verbose_name="Животное", null=True)
    # animal_age = models.ForeignKey('Animal', on_delete=models.CASCADE, help_text="Выберите возраст Животного", verbose_name="Возраст Животного", null=True)
    # animal_life_stage = models.ForeignKey('Animal', on_delete=models.CASCADE, help_text="Выберите период Животного", verbose_name="Период Животного", null=True)
    # animal_weight_animal = models.ForeignKey('Animal', on_delete=models.CASCADE, help_text="Выберите вес Животного", verbose_name="Вес Животного", null=True)
    type_of_goods = models.ForeignKey('TypeOfGoods', on_delete=models.CASCADE, help_text="Выбрать тип продукта", verbose_name="Тип продукта", null=True)
    status = models.ForeignKey('StatusOfGoods', on_delete=models.CASCADE, help_text="Выбрать статус Товара", verbose_name="Статус Товара", null=True)
    objects = models.Manager()

    def __str__(self):
        return '%s %s %s' % (self.name, self.animal, self.price)

