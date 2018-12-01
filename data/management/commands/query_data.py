
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from random import randint
import django
import random

django.setup()

from data.models import Category, Workflow,CategoriesAmount
#models
CATEGORY = 'category'
USER = 'user'
WORKFLOW = 'workflow'
# The name of this class is not optional must  be Command
# otherwise manage.py will not process it properly
class Command(BaseCommand):
    #  args = '<-no arguments>'
    # helps and arguments shown when command python manage.py help populate
    # is executed.
    help = 'This scripts populates de workflow database, no arguments needed.' \
           'Execute it with the command line python manage.py populate'

    def getParragraph(self, init, end):
        # getParragraph returns a parragraph, useful for testing
        if end > 445:
            end = 445
        if init < 0:
            init = 0
        return """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
deserunt mollit anim id est laborum."""[init:end]

    # handle is another compulsory name, This function will be
    # executed by default
    def handle(self, *args, **options):
        self.addCategory("category 1")
        self.addCategory("category 2")
        print "Categorias: "+str(Category.objects.all())+'\n'
        self.addWorkflow("worflow 11", "category 1")
        self.addWorkflow("worflow 12", "category 1")
        self.addWorkflow("worflow 13", "category 1")


        self.addWorkflow("worflow 21", "category 2")
        self.addWorkflow("worflow 22", "category 2")
        self.addWorkflow("worflow 23", "category 2")
        print "Workflows: "+ str(Workflow.objects.all())+'\n'

        self.consulta("category 1")
        self.consulta_slug("workflow-1")
        self.consulta_slug("workflow_10")

    def addCategory(self, category_name):
        categoria = []
        categoria = list(Category.objects.all())
        contador = 0

        for x in categoria:
            if x.name == category_name:
                contador = 1
                break
        if contador == 0:
            categoria.append(Category())
            categoria[len(categoria)-1].name = category_name
            categoria[len(categoria)-1].tooltip="tooltip , ni idea"
            categoria[len(categoria)-1].save()

        # create 5 categories <<<<<<<<<<<<<<<<<<<<<<<
        # baseName, call objects


    def addWorkflow(self, workflow_name, category_name):
        workflow =[]
        categoria = []
        workflow = list(Workflow.objects.all())
        categoria = Category.objects.all()
        i = 0

        for a in categoria:
            if a.name != category_name:
                i +=1
            else:
                break

        contador = 0
        for a in workflow:
            if a.name == workflow_name:
                contador = 1
                break

        if contador == 0:
            workflow.append(Workflow())
            workflow[len(workflow)-1].name = workflow_name
            workflow[len(workflow)-1].description="Esta es la descripcion"
            workflow[len(workflow)-1].views=3
            workflow[len(workflow)-1].downloads=2
            workflow[len(workflow)-1].versionInit="1.0"
            workflow[len(workflow)-1].keywords="palabras clave"
            #workflow.json = self.getJson()
            workflow[len(workflow)-1].save()
            CategoriesAmount.objects.get_or_create(workflow = workflow[len(workflow)-1], categories = categoria[i])
            CategoriesAmount.objects.get_or_create(workflow = workflow[len(workflow)-1], categories = categoria[i])

            workflow[len(workflow)-1].save()

    def consulta(self, category_name):
        workflow =[]
        categoria = []
        workflow = Workflow.objects.all()
        categoria = Category.objects.all()
        i = 0

        for a in categoria:
            if a.name != category_name:
                i +=1
            else:
                break

        filtrado = CategoriesAmount.objects.filter(categories=categoria[i])

        print "Estos son los filtrados con "+category_name+":"+ str(filtrado) + '\n'

    def consulta_slug(self, workflow_slug):
        workflow =[]
        categoria = []
        slugs = []
        workflow = Workflow.objects.all()
        categoria = Category.objects.all()
        i = 0

        for a in workflow:
            if a.slug != workflow_slug:
                i +=1
            else:
                break
        if( i > (len(workflow)-1)):
            print "workflow: " + workflow_slug +" inexistente\n"
            return
        filtrado = CategoriesAmount.objects.filter(workflow=workflow[i])
        for x in filtrado:
            slugs.append(x.categories.slug)
        print "Estos son los filtrados con slug: "+workflow_slug +"-->" +str(slugs) +'\n'
