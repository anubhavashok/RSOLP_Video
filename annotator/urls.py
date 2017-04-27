"""annotator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
import views

urlpatterns = [
    #url(r'^annotator/', TemplateView.as_view(template_name='./annotator/annotation_canvas.html')),
    url(r'^annotator/', views.annotation_canvas),
    url(r'^annotation_canvas_submit_view/', TemplateView.as_view(template_name='./annotator/annotation_submitted.html'), name='annotation_canvas_submit_view'),
    url(r'^admin/', admin.site.urls),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

