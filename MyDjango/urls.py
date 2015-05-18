from django.conf.urls import patterns, url, include
from api import views

    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(api.urls)),
)
