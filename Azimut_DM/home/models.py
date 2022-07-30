from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата обнавления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость' # Наименование в ед. числе
        verbose_name_plural = 'Новости'  # Наименование в мног. числе
        ordering = ['-date_created'] # Сортировка


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'  # Наименование в ед. числе
        verbose_name_plural = 'Категории'  # Наименование в мног. числе
        ordering = ['title']  # Сортировка
