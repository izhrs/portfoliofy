from django.contrib import admin
from django.db import models
from unfold.admin import ModelAdmin, StackedInline
from unfold.contrib.forms.widgets import WysiwygWidget

from .models import Category, Post, PostContent


class PostContentInline(StackedInline):
    model = PostContent
    can_delete = True
    show_change_link = True

    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }


class PostAdmin(ModelAdmin):
    list_display = ('title', 'get_categories', 'featured',
                    'created_at', 'updated_at')
    list_filter = ('categories', 'created_at')
    search_fields = ('title', 'featued', 'categories__name', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PostContentInline]

    # Custom method to display categories in list view
    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    get_categories.short_description = 'Categories'


class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
