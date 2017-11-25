from django import template

register = template.Library()

@register.simple_tag
def getEspot():
    return "yo ssup!!"
