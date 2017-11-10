from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.template import engines


def index(request):
    context = {'latest_question_list': "latest_question_list"}
    return render(request, 'mysite/index.html', context)
    #return HttpResponse("You're at home page on question dededed")
