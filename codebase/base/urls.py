from django.contrib.sitemaps.views import sitemap
from django.urls import path
from django.views.generic.base import TemplateView

from .sitemaps import get_sitemaps
from .views import favicon, home, hx_seach_results, search

urlpatterns = [
    # Sitemaps
    path("sitemap.xml", sitemap, {"sitemaps": get_sitemaps()}, name="django.contrib.sitemaps.views.sitemap"),
    # Search
    path("s/", search, name="search"),
    path("s/results/", hx_seach_results, name="search-results"),
    # Favicon
    path("favicon.ico", favicon, name="favicon"),
    # Home
    path("", home, name="home"),
    # robots.txt
    path(
        "robots.txt",
        TemplateView.as_view(template_name="base/robots.txt", content_type="text/plain"),
    ),
]
