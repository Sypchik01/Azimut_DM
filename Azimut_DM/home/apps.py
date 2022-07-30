from django.apps import AppConfig


class HomePageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
    verbose_name = 'Новости' #Название шапки в админке