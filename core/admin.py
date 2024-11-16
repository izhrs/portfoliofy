from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from django.db import models
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.forms import UserChangeForm

from .forms import CustomUserCreationForm
from .models import Project, Testimonial

admin.site.unregister(User)
admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin, ModelAdmin):
    add_form = CustomUserCreationForm  # Use the custom form for user creation
    form = UserChangeForm  # Use the custom form for user editing
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )


class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


class ProjectAdmin(ModelAdmin):
    list_display = ('title', 'category', 'description', 'updated_at')
    search_fields = ('title', 'category', 'description')
    list_filter = ('category', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }


class TestimonialAdmin(ModelAdmin):
    list_display = ('name', 'designation', 'created_at', 'updated_at')
    search_fields = ('name', 'designation', 'quote')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
