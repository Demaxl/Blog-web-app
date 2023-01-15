from django.contrib import admin
from django.utils.html import format_html
from imagekit.admin import AdminThumbnail


from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display_links = ("first_name", "last_name", "joined_date",)
    list_display = ("first_name", "last_name", "joined_date")


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("author", "subject", "publish_date")
    date_hierarchy = "publish_date"


