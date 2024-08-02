from django import template

register = template.Library()

@register.filter(name='custom_range')
def custom_range(value, start=0):
    return range(start, value)

@register.filter(name='range_filter')
def range_filter(start, end):
    return range(start, end)
