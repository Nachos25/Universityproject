from django import template

register = template.Library()


@register.simple_tag()
def underscoreTag(obj, attribute):
    obj = dict(obj)
    print(obj)
    print(obj.get(attribute))
    return obj.get(attribute)