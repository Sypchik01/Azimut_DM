# Generated by Django 4.0.6 on 2022-08-01 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Наименование')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Дата обнавления')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-date_created'],
            },
        ),
    ]
