from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from codebase.base.utils.actions import translation_actions
from codebase.base.utils.admin import FORMFIELD_OVERRIDES_DICT

from .models import Home, HomeHeroSection


@admin.register(Home)
class HomeAdmin(TranslationAdmin):
    formfield_overrides = FORMFIELD_OVERRIDES_DICT
    actions = translation_actions
    list_display = ("__str__", "title", "site")


@admin.register(HomeHeroSection)
class HomeHeroAdmin(TranslationAdmin):
    list_display = ("headline", "cta_link", "image", "is_active", "allow_translation")
    list_editable = ("is_active", "cta_link", "image", "allow_translation")
    list_filter = ("home", "is_active", "allow_translation")
    actions = translation_actions
