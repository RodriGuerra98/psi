# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from data.models import Category, Workflow, CategoriesAmount

class CategoryInline(admin.TabularInline):
    model = CategoriesAmount
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name', 'slug')

class WorkflowAdmin(admin.ModelAdmin):
    list_display=('name', 'slug', 'views', 'downloads', 'client_ip', 'created')
    inlines = (CategoryInline,)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Workflow, WorkflowAdmin)
