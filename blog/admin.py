from django.contrib import admin
from .models import Blog,Comment


@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):

    list_display = ('entry_title', 'entry_author', 'entry_date')
    list_filter = ('entry_date', 'entry_author')
    search_fields = ('enrty_title', 'entry_text')
    raw_id_fields = ('entry_author',)
    date_hierarchy = 'entry_date'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)