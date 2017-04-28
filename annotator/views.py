from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings




def annotation_canvas(request):
    context = {'STATIC_URL': settings.STATIC_URL}
    #return TemplateView.as_view(template_name='annotator/annotation_canvas.html')
    return render(request, 'annotator/annotation_canvas.html', context)

def annotation_canvas_submit_view(request):
    context = {}#{'STATIC_URL': settings.STATIC_URL}
    #return TemplateView.as_view(template_name='annotator/annotation_canvas.html')
    return render(request, 'annotator/annotation_submitted.html', context)
