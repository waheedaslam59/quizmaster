import os

from django import template


register = template.Library()

@register.filter
def mytags(value):
    return os.path.basename(value.file.name)