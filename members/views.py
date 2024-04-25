from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Members

def members(request):
    template = loader.get_template('myfirst.html')
    mymembers = Members.objects.all().values()
    context ={
        'mymembers':mymembers
    }
    return HttpResponse(template.render(context,request))
def details(request,id):
    template = loader.get_template('details.html')
    mymember = Members.objects.get(id=id)
    context ={
        'mymember':mymember,
    }
    return HttpResponse(template.render(context, request))