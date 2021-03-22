from django import template
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()

@register.filter(name='calculations')
def calculations(value, args):
    if args == 'modulus':
        return value%7