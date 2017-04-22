from django.http import HttpResponse
from django.template import loader
import settings

def annotation_create(request):
    template = loader.get_template('annotator/annotation_create.html')
    return HttpResponse(template.render({}, request))



def annotation_canvas(request):
    template = loader.get_template('annotator/annotation_canvas.html')
    return HttpResponse(template.render({'STATIC_URL': '../static/'}, request))

def annotation_list(request):
    template = loader.get_template('annotator/annotation_list.html')
    return HttpResponse(template.render({}, request))

def annotation_submitted(request):
    template = loader.get_template('annotator/annotation_submitted.html')
    return HttpResponse(template.render({}, request))

