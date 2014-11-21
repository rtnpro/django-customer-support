from __future__ import absolute_import
from django.shortcuts import render
import simplejson
import datetime
from django.http import HttpResponse


class GenericItem(object):
    ITEM_ATTRS = []
    TEMPLATE = 'customer_support/item.html'

    def __init__(self, item_id):
        self._item_id = item_id
        self._context = None

    def _get_context(self):
        if self._context:
            for key, value in self.get_item_data(self._item_id):
                if key in self.ITEM_ATTRS:
                    self._context[key] = value
        return self._context

    def get_item_data(self, item_id):
        raise NotImplementedError

    def render_html(self):
        return render(self.TEMPLATE, {'item_data': self._get_context()})

    def jsonify(self, value):
        """
        Method to convert non JSON serializable objects into
        an equivalent JSON serializable form.
        """
        return value

    def set_item_data(self, data):
        self._context = {}
        for key, value in data.items():
            if key in self.ITEM_ATTRS:
                self._context[key] = value

    def json(self):
        context = self._get_context()
        _context = {}
        for attr_name in self.ITEM_ATTRS:
            attr = self.jsonify(context[attr_name])
            if isinstance(attr, datetime):
                attr = attr.strftime('%Y-%m-%d %H:%M')
            _context[attr_name] = attr
        return simplejson.dumps(_context)

    def render_json(self):
        return HttpResponse(
            self.json(), mimetype='application/json')
