# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from upload.forms import WorkflowForm
from data.models import Category, Workflow,CategoriesAmount
from find import views

# Create your views here.

def add_workflow(request):
    form = WorkflowForm()

    if( request.method() == 'POST'):
        form = WorkflowForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return workflow_list(request)
        else:
            print(form.errors)
    categories = Category.objects.all()

    return render(request, 'upload/add_workflow.html', {'form' : form, 'categories' : categories})
