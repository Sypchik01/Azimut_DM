from django.contrib import admin

from .models import News, Category

#Выводимые поля в админке
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_created', 'date_update', 'is_published', 'category',)
    list_display_links = ('id', 'title') #Делает поля ссылкой
    search_fields = ('title', 'content') #Поиск по полям
    list_editable = ('is_published',) #Редактирование из основного окна
    list_filter = ('is_published', 'category') #Сортировка


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',) #Делает поля ссылкой
    search_fields = ('title',) #Поиск по полям


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
