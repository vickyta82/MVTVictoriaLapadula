from django.http import HttpResponse
from django.template import Template, Context

def home_page(request):
    return HttpResponse("Welcome to Your Phone Book!")

def family_members(request):
    file = open(r"C:\Users\vlapa\Desktop\Python\MVTVictoriaLapadula\MVTVL\MVTVL\templates\family.html", 'r')
    template = Template(file.read())
    file. close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)

