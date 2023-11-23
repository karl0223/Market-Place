from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Category)
class CatergoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name__istartswith"]


@admin.register(models.Item)
class ItemsAdmin(admin.ModelAdmin):
    autocomplete_fields = ["category", "created_by"]
    list_display = [
        "category",
        "name",
        "description",
        "price",
        "image",
        "is_sold",
        "created_by",
        "created_at",
    ]
    list_select_related = ["category", "created_by"]
