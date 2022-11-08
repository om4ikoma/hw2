from django.contrib import admin
from main.models import Film, Director


class Films(admin.ModelAdmin):
    list_display = ['name']
    search_fields = 'id title text'.split()
    list_per_page = 3


admin.site.register(Film)
admin.site.register(Director)

