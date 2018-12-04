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
            form.save(commit=True)
            return views.workflow_list(request)
        else:
            print(form.errors)
    categories = Category.objects.all()



    return render(request, 'upload/add_workflow.html', {'form' : form, 'categories' : categories})
