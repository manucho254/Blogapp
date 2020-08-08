from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    list_display = ('entry_title', 'entry_author', 'entry_date')
    list_filter = ('entry_date', 'entry_author')
    search_fields = ('enrty_title', 'entry_text')
    raw_id_fields = ('entry_author',)
    date_hierarchy = 'entry_date'