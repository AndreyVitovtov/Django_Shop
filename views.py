from django.template import loader
from django.http import HttpResponse

def project_1(request):
    template = loader.get_template("Categories_template.html")
    return HttpResponse(template.render())

def project_2(request):
  template = loader.get_template("Product_template.html")
  return HttpResponse(template.render())

