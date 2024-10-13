from modeltranslation.translator import TranslationOptions, register

from .models import FooterItem, NavbarItem, PageLink


@register(NavbarItem)
class NavbarItemOptions(TranslationOptions):
    fields = ("title", "slug")


@register(FooterItem)
class FooterItemOptions(TranslationOptions):
    fields = ("title", "slug")


@register(PageLink)
class PageLinkOptions(TranslationOptions):
    fields = ("custom_title",)
