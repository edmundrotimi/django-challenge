from django import template
register = template.Library()


@register.filter(name='bold', is_safe=True)
def boldvalue(value, arg=500):
    return  f'<span style="font-weight:{arg};">{value}</span>'