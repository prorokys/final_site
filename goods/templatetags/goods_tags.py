from goods.models import Categories

from django import template


register = template.Library()


@register.simple_tag()
def categories_tag():
    return Categories.objects.all()
