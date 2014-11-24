from __future__ import absolute_import
from django.shortcuts import render
import simplejson
import datetime
from django.http import HttpResponse


class GenericItemBase(object):
    ITEM_ATTRS = []

    def __init__(self, identifier):
        self.identifier = identifier

    def jsonify(self, value):
        """
        Method to convert non JSON serializable objects into
        an equivalent JSON serializable form.
        """
        return value

    def json(self):
        raise NotImplementedError

    def render_json(self):
        raise NotImplementedError

    def render_html(self):
        raise NotImplementedError


class GenericItem(GenericItemBase):
    TEMPLATE = 'customer_support/item.html'

    def __init__(self, *args, **kwargs):
        super(GenericItem, self).__init__(*args, **kwargs)
        self._item = {}

    def get_item(self, identifier):
        raise NotImplementedError

    def set_item(self, data):
        self._item = {}
        for key, value in data.items():
            if key in self.ITEM_ATTRS:
                self._item[key] = value

    def json(self):
        item = {}
        for attr_name in self.ITEM_ATTRS:
            attr = self.jsonify(self._item[attr_name])
            if isinstance(attr, datetime):
                attr = attr.strftime('%Y-%m-%d %H:%M')
            item[attr_name] = attr
        return simplejson.dumps(item)

    def render_json(self):
        return HttpResponse(
            self.json(), mimetype='application/json')

    def render_html(self):
        return render(self.TEMPLATE, {'item': self._item})


class GenericItems(GenericItemBase):
    TEMPLATE = 'customer_support/items.html'

    def __init__(self, *args, **kwargs):
        super(GenericItem, self).__init__(*args, **kwargs)
        self._items = []

    def get_items(self, for_entity):
        raise NotImplementedError

    def set_items(self, items):
        self._items = items

    def json(self):
        items = []
        for item in self._items:
            item_dict = {}
            for attr_name in self.ITEM_ATTRS:
                attr = self.jsonify(item[attr_name])
                if isinstance(attr, datetime):
                    attr = attr.strftime('%Y-%m-%d %H:%M')
                item_dict[attr_name] = attr
            items.append(item)
        return simplejson.dumps(items)

    def render_json(self):
        return HttpResponse(
            self.json(), mimetype='application/json')

    def render_html(self):
        return render(self.TEMPLATE, {'items': self._items})
