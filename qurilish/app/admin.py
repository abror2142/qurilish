from django.contrib import admin
from .models import Hudud, Qurilish, QurilishTashkiloti


@admin.register(Hudud)
class HududAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']


@admin.register(Qurilish)
class QurilishAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'hudud', 'qurilish_tashkiloti']
    list_display_links = ['name']
    
    
@admin.register(QurilishTashkiloti)
class QurilishTashkilotiAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'hudud']
    list_display_links = ['name']