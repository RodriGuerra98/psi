  # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from upload.forms import WorkflowForm
from data.models import Category, Workflow,CategoriesAmount
from find import views


# Create your views here.

def add_workflow(request):
    form = WorkflowForm()
    status = True
    error = ""
    result = True
    if request.method == 'POST':

        form=WorkflowForm(request.POST, request.FILES)

        if form.is_valid():

            workflow=form.save(commit=True)
            _dict = {}
            _dict['result'] = True
            _dict['workflow'] = workflow
            _dict['error']="Error al cargar los detalles"
            _dict['categories'] = []
            _dict['delete'] = True
            try:
                categories = CategoriesAmount.objects.filter(workflow = workflow )
            except ObjectDoesNotExist:
                result = False
                error = "Todavia no hay categorias para asociar a un Workflow"

            categories_aux = []
            for x in categories:
                categories_aux.append(Category.objects.get(id=x.categories.id))
            _dict['categories'] = categories_aux

            return render (request, "find/detail.html",context = _dict )
        else:
            print(form.errors)
            status = False


    categories = Category.objects.all()



    return render(request, 'upload/add_workflow.html', {'form' : form, 'categories' : categories, 'status' : status})
