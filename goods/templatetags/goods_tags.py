from goods.models import Categories
from django.utils.http import urlencode
from django import template


register = template.Library()


@register.simple_tag()
def categories_tag():
    return Categories.objects.all()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context["request"].GET.dict()
    query.update(kwargs)
    return urlencode(query)
