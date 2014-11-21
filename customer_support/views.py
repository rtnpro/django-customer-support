from __future__ import absolute_import
from django.views.generic.base import View
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
import simplejson
from .conf import CUSTOMER_SUPPORT_SCHEMA_FUNC


class CustomerSupport(View):

    def get(self, request):
        context = getattr(settings, 'CUSTOMER_SUPPORT_SCHEMA_FUNC',
                          CUSTOMER_SUPPORT_SCHEMA_FUNC)()
        if request.GET.get('format', '').lower() == 'json':
            return HttpResponse(
                simplejson.dumps(context), mimetype='application/json')
        return render(
            request, getattr(
                settings, 'CUSTOMER_SUPPORT_PAGE_TEMPLATE',
                'customer_support/pages.html'), context)
