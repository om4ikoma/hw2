from django.contrib import admin
from main.models import Film, Director


class FilmAdmin(admin.ModelAdmin):
    list_display = ['director', 'title', 'rating', 'duration', ]
    search_fields = 'title'.split()
    list_filter = ['director', 'title', 'rating', 'duration', ]
    list_display_links = None
    list_editable = 'director title rating'.split()


admin.site.register(Film, FilmAdmin)
admin.site.register(Director)
