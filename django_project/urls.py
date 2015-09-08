from django.conf.urls import include, url
from django.contrib import admin

from assesment import urls as assesment_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(assesment_urls)),
]
