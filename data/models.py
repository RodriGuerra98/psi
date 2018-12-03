# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.postgres.fields import JSONField
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(blank=False, unique=True, max_length=128)
    slug = models.SlugField(blank=True, unique=True, max_length=512)
    created = models.DateField(default=datetime.date.today) #esta bien pero mejor la base de datos, mirar documentacion de DateField
    tooltip = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.slug =  slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural='Categories'

    def  __str__(self):
        return self.name

class Workflow(models.Model):
    name = models.CharField(blank=False, unique=True, max_length=255) #AUMENTADO
    slug = models.SlugField(blank=True, unique=True, max_length=512)
    created = models.DateField(default=datetime.date.today)
    category = models.ManyToManyField(Category, through ='CategoriesAmount')
    keywords = models.CharField(max_length=512, default="")
    description = models.CharField(max_length=512, default="")
    views = models.IntegerField(default = 0)
    downloads = models.IntegerField(default =0)
    versionInit = models.CharField(max_length=512)
    client_ip = models.GenericIPAddressField(default='127.0.0.1')
    #json = JSONField()

    def save(self, *args, **kwargs):
        self.slug =  slugify(self.name)
        super(Workflow, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural='Workflows'

    def  __str__(self):
        return self.name

class CategoriesAmount(models.Model):
    workflow = models.ForeignKey(Workflow,on_delete=models.CASCADE)
    categories= models.ForeignKey(Category,on_delete=models.CASCADE)

    def  __str__(self):
        return str(self.workflow) + "-->"+ str(self.categories)
