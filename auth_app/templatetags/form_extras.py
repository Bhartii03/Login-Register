from django import template

register = template.Library()

@register.filter
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})

from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={'class': css_class})