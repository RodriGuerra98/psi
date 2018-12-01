# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import render
from data.models import Category, Workflow,CategoriesAmount
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
import json
def workflow_list(request, category_slug=None):

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
        cat = CategoriesAmount.objects.all()
        for x in cat:
            if x.categories.slug == category_slug:
                workflows.append(x.workflow)
                category = x
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
    _dict = {'category': category,  # category associated to category_slug
    'categories': categories,  # list with all categories
    # usefull to repaint the category
    # menu
    'workflows': workflows,    # all workflows associated to category
    # category_slug
    'result': found,           # False if no workflow satisfices the query
    'error': error,             # message to display if results == False
    'workflows_p': workflows_p
    }
    return render(request, 'list.html', context=_dict )

def workflow_detail(request, id, slug):
    workflows = Workflow.objects.all()
    _dict = {}
    result= True
    error = ""
    workflow = None
    print workflows

    for x in workflows:
        if(str(x.id)==str(id)):
            workflow = x
            result= True
            error = ""
            break
        else:
            result = False
            error = "Error en escoger un workflow"
    all = Category.objects.all()
    categories_aux = CategoriesAmount.objects.filter(workflow=workflow)
    categories = []
    for y in all:
        for z in categories_aux:
            if(str(y.id)==str(z.id)):
                categories.append(y)


    _dict['result'] = result      # False if no workflow satisfices the query
    _dict['workflow'] = workflow  # workflow with id = id
    _dict['error'] = error        # message to display if results == False
    _dict['categories'] = []
    _dict['categories'] = categories
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
