from django.contrib import admin
from .models import *

class AutorAdmin(admin.ModelAdmin):

    list_display = ('name', 'surename', 'fathername', 'city', 'birthday') # то что мы хотим выводить в таблице
    list_display_links = ('name', 'surename')  # какие поля будут ссылками
    search_fields = ('name', 'surename')  # по каким полям будет происходить поиск
    # list_editable = ()  # какие поля можно редактировать сразу в таблице
    # list_filter = ('airport_name',)  # для вывода боковых фильтров вывода

class BooksAdmin(admin.ModelAdmin):

    list_display = ('name', 'write_date', 'description', 'pages', 'image', 'autor_relative')
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Autor, AutorAdmin)
admin.site.register(Books, BooksAdmin)
