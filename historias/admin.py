from django.contrib import admin
from .models import Historia


@admin.register(Historia)
class HistoriaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'nombre', 'lugar_origen', 'personajes', 'estado', 'fecha_envio']
    list_filter = ['estado']
    search_fields = ['nombre', 'lugar_origen', 'historia']
    list_editable = ['estado']
