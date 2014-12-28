from django.conf.urls import patterns, include, url

import example.urls

urlpatterns = patterns("",
    url(r"^autocomplete/", include("autocomplete_light.urls")),
    url(r"^$", include("example.urls")),
)
