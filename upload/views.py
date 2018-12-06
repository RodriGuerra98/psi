  # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from upload.forms import WorkflowForm
from data.models import Category, Workflow,CategoriesAmount
from find import views


# Create your views here.

def add_workflow(request):
    form = WorkflowForm()
    if request.method == 'POST':

        form=WorkflowForm(request.POST, request.FILES)

        if form.is_valid():
            print "posta 1"

            workflow=form.save(commit=True)
            _dict = {}
            _dict['result'] = True
            _dict['workflow'] = workflow
            _dict['error']="Error al cargar los detalles"
            _dict['categories'] = []
            categories = CategoriesAmount.objects.filter(workflow = workflow )
            categories_aux = []
            for x in categories:
                categories_aux.append(Category.objects.get(id=x.categories.id))
            _dict['categories'] = categories_aux

            return render (request, "find/detail.html",context = _dict )
        else:
            print(form.errors)
    categories = Category.objects.all()



    return render(request, 'upload/add_workflow.html', {'form' : form, 'categories' : categories})
