from django.contrib import admin

from .models import Project, Testimonial


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'category', 'description')
    list_filter = ('category', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'created_at', 'updated_at')
    search_fields = ('name', 'designation', 'quote')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
