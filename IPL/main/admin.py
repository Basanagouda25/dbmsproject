from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Teams)
class Teams(admin.ModelAdmin):
    list_display=('name',)

@admin.register(bowlers)
class bowlers(admin.ModelAdmin):
    list_display=('player','role')

@admin.register(batsmen)
class batsmen(admin.ModelAdmin):
    list_display=('player','role')

@admin.register(allrounder)
class Allrounder(admin.ModelAdmin):
    list_display=('player','bowling_role','batting_role')