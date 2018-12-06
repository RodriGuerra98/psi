# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect

import urllib
import urllib2
import json
from data.models import Category, Workflow,CategoriesAmount
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
import json

status = True
def workflow_list(request, category_slug=None):
    global status
    status = True
    page = request.GET.get('page', 1)
    categories=[]
    categories = Category.objects.all()
    found = True
    error = ""
    category = None
    workflows=[]
    if category_slug == None:
        workflows= list(Workflow.objects.all())

    else:
        category = Category.objects.get(slug=category_slug)
        cat = CategoriesAmount.objects.filter(categories=category)
        for x in cat:
            workflows.append(Workflow.objects.get(id=x.workflow.id))
        if len(workflows) == 0:
            found=False
            error = "Error"

    paginator = Paginator(workflows, 10)
    try:
        workflows_p = paginator.page(page)
    except PageNotAnInteger:
        usworkflows_p = paginator.page(1)
    except EmptyPage:
        workflows_p = paginator.page(paginator.num_pages)



    # YOUR CODE GOES HERE
    # queries that fill, category, categories, workflows
    # and erro
    _dict = {
        'category': category,      # category associated to category_slug
        'categories': categories,  # list with all categories
        'workflows': workflows,    # all workflows associated to category
        'result': found,           # False if no workflow satisfices the query
        'error': error,            # message to display if results == False
        'workflows_p': workflows_p
    }
    return render(request, 'find/list.html', context=_dict )

def workflow_detail(request, id, slug):
    global status
    _dict = {}
    result= True
    error = ""
    workflow = None
    try:
        workflow = Workflow.objects.get(id=id)
    except ObjectDoesNotExist:
        result = False
        error = "Error en buscar un workflow con nombre"
        print "El workflow con ese nombre no existe"

    categories = CategoriesAmount.objects.filter(workflow = workflow )
    categories_aux = []
    for x in categories:
        categories_aux.append(Category.objects.get(id=x.categories.id))


    _dict['result'] = result      # False if no workflow satisfices the query
    _dict['workflow'] = workflow  # workflow with id = id
    _dict['error'] = error        # message to display if results == False
    _dict['categories'] = []
    _dict['categories'] = categories_aux
    _dict['status'] = status
    return render(request, "find/detail.html", context = _dict)

def workflow_search(request):
#YOUR CODE GOES HERE
#query that returns the workflow with name = name
    name = request.POST.get('key')
    type = request.POST.get('selector')
    workflow = None
    categories = None
    result= True
    error = ""

    if type == 'name':
        try:
            workflow = Workflow.objects.get(name=name)
        except ObjectDoesNotExist:
            result = False
            error = "Error en buscar un workflow con nombre"
            print "El workflow con ese nombre no existe"
    else :
        try:
            workflow = Workflow.objects.get(slug=name)
        except ObjectDoesNotExist:
            result = False
            error = "Error en buscar un workflow con slug"
            print "El workflow con ese slug no existe"

    _dict = {}
    _dict['result'] = result      # False if no workflow satisfices the query
    _dict['workflow'] = workflow  # workflow with name = name
    _dict['error'] = error        # message to display if results == False
    _dict['categories'] = []
    _dict['categories'] = categories
    return render(request, 'find/detail.html', context= _dict)


def workflow_download(request, id ,slug, count = True):
    global status
    ''' Begin reCAPTCHA validation '''
    recaptcha_response = request.POST.get('g-recaptcha-response')
    url = 'https://www.google.com/recaptcha/api/siteverify'
    values = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    result = json.load(response)
    print "VALIDACION RECAPTCHA"
    print result
    ''' End reCAPTCHA validation '''

    if result['success']:
        messages.success(request, 'New comment added with success!')
        print "EL CAPTCHA SE HA RELLENADO"
        workflow =  Workflow.objects.get(id = id)
        if workflow is None :
            return
        workflow.downloads +=1
        if count is True:
            workflow.views+=1
        workflow.save()
        response = HttpResponse ( workflow.json, content_type="application/octet-stream")
        fileName = "salida.json"
        response['Content-Disposition']= 'inline; filename= %s' %fileName
        return response
    else:
        status=False
        messages.error(request, 'Invalid reCAPTCHA. Please try again.')

    return redirect('workflow_detail', id = id , slug = slug)

def workflow_download_json(request, id , slug):
    try:
        workflow =  Workflow.objects.get(id = id)
        print workflow
    except ObjectDoesNotExist:
        print "El workflow con ese slug no existe"

    return HttpResponse ( workflow.json, content_type="application/octet-stream")
