from django.contrib import admin

from children.models import NaughtyAndNice


@admin.register(NaughtyAndNice)
class NaughtyAndNiceAdmin(admin.ModelAdmin):
    list_display = ('child_name', 'actions', 'wish')