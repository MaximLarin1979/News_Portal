from django.contrib import admin
from .models import Post, Category, Comment


# напишем уже знакомую нам функцию обнуления товара на складе
def nullfy_quantity(modeladmin, request, queryset):  # все аргументы уже должны быть вам знакомы, самые нужные из них
    # это request — объект хранящий информацию о запросе и queryset — грубо говоря набор объектов, которых мы
    # выделили галочками.
    queryset.update(quantity=0)


nullfy_quantity.short_description = 'Обнулить статьи'  # описание для более понятного представления в админ панели


# задаётся, как будто это объект


class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('post_name', 'post_type', 'post_rating', 'post_time', 'author')
    # необязательно поле, можно прописать функцию, например (в модели) и добавить как поле вывода
    list_filter = ('post_name', 'post_type', 'post_rating', 'post_time', 'author')
    # простые фильтры
    search_fields = ('post_name', 'author')
    # больше похоже на фильтры
    actions = [nullfy_quantity]  # добавляем действия в список


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
