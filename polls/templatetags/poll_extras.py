from django import template
import requests
import json
from django.http import Http404, HttpResponse
import datetime
from django.utils.safestring import mark_safe
register = template.Library()

@register.simple_tag
def getEspot():
    ur = "url"
    #response = requests.get('https://api.github.com/user/chao420456')
    response = requests.get(ur)
    data = response.json()['MarketingSpotData'][0]['baseMarketingSpotActivityData'][0]
    data = data['marketingContentDescription'][0]['marketingText']
    #return data
    return mark_safe(data)
