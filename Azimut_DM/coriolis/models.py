from django.db import models


class Banner(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Баннер' # Наименование в ед. числе
        verbose_name_plural = 'Баннеры'  # Наименование в мног. числе
        ordering = ['name'] # Сортировка


class Advantage(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.IntegerField(null=True, verbose_name='Цена')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    advantage_type = models.ForeignKey('AdvantageType', on_delete=models.PROTECT, null=True, verbose_name='Типы достоинств')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Достоинство' # Наименование в ед. числе
        verbose_name_plural = 'Достоинства'  # Наименование в мног. числе
        ordering = ['name'] # Сортировка


class AdvantageType(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Достоинства'  # Наименование в ед. числе
        verbose_name_plural = 'Типы достоинства'  # Наименование в мног. числе
        ordering = ['name']  # Сортировка