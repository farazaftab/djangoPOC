from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', views.index, name='index'),
	#url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
	#url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]