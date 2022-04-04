from multiprocessing import context
from django.http import HttpResponse
from django.template import Template, Context, loader

def home_page(request):
    return HttpResponse("Welcome to Your Phone Book!")

def family_members(request):
    template = loader.get_template("family.html")
    document = template.render() 
    return HttpResponse(document)
