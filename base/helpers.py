import re

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def formatoNumero(value): 
    valor = '{:,}'.format(value).replace(',','.')
    return valor

@register.filter
def negate(boolean):
    return (not boolean).__str__()