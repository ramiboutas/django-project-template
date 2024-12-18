from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Article, ArticleFile, ArticleParentFolder


@admin.register(ArticleParentFolder)
class ArticlesSubmoduleAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    list_display = (
        "title",
        "folder_name",
        "subfolder_name",
        "created_on",
        "updated_on",
    )
    readonly_fields = (
        "title",
        "parent_folder",
        "folder_name",
        "subfolder_name",
        "body",
        "created_on",
        "updated_on",
    )
    list_filter = ("parent_folder", "folder_name", "created_on", "updated_on")
    search_fields = ("title", "folder_name", "subfolder_name", "body")


@admin.register(ArticleFile)
class ArticleFileAdmin(admin.ModelAdmin):
    list_display = ("name", "article", "file")
    readonly_fields = ("name", "article", "file")
