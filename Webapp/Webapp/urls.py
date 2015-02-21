from django.conf.urls import patterns, include, url
from django.contrib import admin

from info_chantier import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.nfc),
    url(r'^subscrib$', views.subscrib),
    url(r'^walk$', views.walk),
    url(r'^unset$', views.unset),
    url(r'^end$', views.end),
    url(r'^admin/', include(admin.site.urls)),
)
