from django.contrib import admin

from .models import *

#Выводимые поля в админке
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'advantage_type', 'description', 'price', 'image', 'is_published',)
    list_display_links = ('id', 'name',) #Делает поля ссылкой
    search_fields = ('name', 'description') #Поиск по полям
    list_filter = ('name', 'advantage_type') #Сортировка


class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo','prioritet',)
    list_display_links = ('id', 'name',) #Делает поля ссылкой
    search_fields = ('name',) #Поиск по полям


class AdvantageTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',) #Делает поля ссылкой


class RegulationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',) #Делает поля ссылкой


class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',) #Делает поля ссылкой


admin.site.register(Advantage, AdvantageAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(AdvantageType, AdvantageTypeAdmin)
admin.site.register(Regulation, RegulationAdmin)
admin.site.register(Description, DescriptionAdmin)
