#-*- coding: utf-8 -*-
import base64
import json
import math

from django import template
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.html import mark_safe

from main.serializers.json import ModelReprEncoder

register = template.Library()


@register.simple_tag
def nav_active(request, urls, cls='active'):
    if request.path in (reverse(url) for url in urls.split()):
        return cls
    return ""

@register.filter
def nav_url(request, url):
    return url in request.path


@register.filter
def add_class(value, arg):
    cls = value.field.widget.attrs.get('class')
    return value.as_widget(attrs={'class': cls + ' ' + arg if cls else '' + arg})


@register.filter
def jsonify(o):
    """
    Перевод объект в json
    :param o:
    :return:
    """
    return mark_safe(json.dumps(o, cls=ModelReprEncoder))


@register.filter
def jsonify_html(o):
    """
    Перевод объект в json
    :param o:
    :return:
    """
    return json.dumps(o, cls=ModelReprEncoder)


@register.filter
def base64encode(o):
    return base64.b64encode(jsonify_html(o).encode('utf-8'))


@register.filter
def fmt_date(date):
    """
    Форматирует дату
    :param date:
    :return:
    """
    try:
        now = timezone.localtime(timezone.now())
        local = timezone.localtime(date)
        yesterday = now - timezone.timedelta(days=1)
        if local.date() == now.date():
            return 'Сегодня в '+str(local.strftime('%H:%M'))
        if local.date() == yesterday.date():
            return 'Вчера в '+str(local.strftime('%H:%M'))
        return local.strftime('%d.%m.%y в %H:%M')
    except:
        return ''


@register.filter
def attr(object, attribute):
    """
    получает атрибут объекта
    :param object:
    :param attribute:
    :return:
    """
    return object.get(attribute, None)
