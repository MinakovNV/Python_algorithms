from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from otziv.models import Otziv


@admin.register(Otziv)
class OtzivAdmin(admin.ModelAdmin):
    list_display = ('get_film_name', 'name', 'email', 'date')
    search_fields = ('film__name', 'name', 'email',)
    list_filter = (
        ('date', DateFieldListFilter),
    )
