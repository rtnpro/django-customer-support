from __future__ import absolute_import
from django.conf.urls import patterns, url
from .views import CustomerSupport

urlpatterns = patterns(
    '',
    url(r'^$', CustomerSupport.as_view(), name='customer_support')
)
