from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "is_published", "published_at")
    list_filter = ("is_published",)
    search_fields = ("title", "excerpt", "content")
