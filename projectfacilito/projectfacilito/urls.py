
from django.contrib import admin
from django.urls import path,include

from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/',include('book.urls')),

    url(r'^.*$',TemplateView.as_view(template_name='index.html')),
]
