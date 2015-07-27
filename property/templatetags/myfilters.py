from django.template import Library

register = Library()

@register.filter
def get_range(value):
    return range(int(value))

@register.filter
def subtract(value, arg):
    return int(value) - int(arg)
