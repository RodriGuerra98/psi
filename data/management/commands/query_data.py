
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
        self.addWorkflow("worflow 11", "category 1")
        self.addWorkflow("worflow 12", "category 1")
        self.addWorkflow("worflow 13", "category 1")


        self.addWorkflow("worflow 21", "category 2")
        self.addWorkflow("worflow 22", "category 2")
        self.addWorkflow("worflow 23", "category 2")

        self.consulta("category 1")
        self.consulta_slug("workflow-1")
        self.consulta_slug("workflow_10")

    def addCategory(self, category_name):

        categoria = Category.objects.filter(name = category_name)
        if len(categoria) == 0:
            categoria = Category()
            categoria.name = category_name
            categoria.save()
            return
        else:
            print "Error categoria "+category_name+" ya existente"

        # create 5 categories <<<<<<<<<<<<<<<<<<<<<<<
        # baseName, call objects


    def addWorkflow(self, workflow_name, category_name):
        workflow = Workflow.objects.filter(name = workflow_name)
        if len(workflow) == 0:
            workflow = Workflow()
            workflow.name = workflow_name
            workflow.json = getJson(self)
            categoria=Category.objects.filter(name = category_name)
            if len(categoria) == 0:
                print "Categoria no encontrada al anadir el workflow: "+ category_name
                return
            workflow.save()
            CategoriesAmount.objects.get_or_create(workflow = workflow, categories = categoria[0])
            workflow.save()
            return
        else:
            print "Error workflow "+workflow_name+" ya existente"



    def consulta(self, category_name):
        categoria = Category.objects.filter(name = category_name)
        if len(categoria) == 0:
            print "Categoria no encontrada al hacer el filtrado"
            return
        filtrado = CategoriesAmount.objects.filter(categories=categoria[0])
        if len(filtrado) == 0:
            print "No existen workflows para categoria"+category_name+"\n"
        else:
            print "Estos son los filtrados de la categoria "+category_name+":\n"
            print filtrado
            print '\n'


    def consulta_slug(self, workflow_slug):
        workflow = Workflow.objects.filter(slug=workflow_slug)
        if len(workflow) == 0:
            print "No existe worflow con slug"+workflow_slug+"\n"
            return

        filtrado = CategoriesAmount.objects.filter(workflow=workflow[0])
        if len(filtrado) == 0:
            print "El workflow no pertenece a niguna categoria"
        else:
            print "Estos son los filtrados del workglow (slug): "+workflow_slug +":"
            print filtrado
            print '\n'

def getJson(self):
    return """[
{
    "object.className": "ProtImportMovies",
    "object.id": "2",
    "object.label": "import movies",
    "object.comment": "\\n",
    "runName": null,
    "runMode": 0,
    "importFrom": 0,
    "filesPath": "",
    "filesPattern": "Falcon*.mrcs",
    "copyFiles": false,
    "acquisitionWizard": null,
    "voltage": 300.0,
    "sphericalAberration": 2.0,
    "amplitudeContrast": 0.1,
    "magnification": 39548,
    "samplingRateMode": 0,
    "samplingRate": 3.54,
    "scannedPixelSize": 14.0,
    "gainFile": null
},
{
    "object.className": "ProtMovieAlignment",
    "object.id": "40",
    "object.label": "movie alignment",
    "object.comment": "\\n",
    "runName": null,
    "runMode": 0,
    "cleanMovieData": true,
    "alignMethod": 0,
    "alignFrame0": 0,
    "alignFrameN": 0,
    "doGPU": false,
    "GPUCore": 0,
    "winSize": 150,
    "sumFrame0": 0,
    "sumFrameN": 0,
    "cropOffsetX": 0,
    "cropOffsetY": 0,
    "cropDimX": 0,
    "cropDimY": 0,
    "binFactor": 1,
    "extraParams": "",
    "hostName": "localhost",
    "numberOfThreads": 4,
    "numberOfMpi": 1,
    "inputMovies": "2.__attribute__outputMovies"
},
{
    "object.className": "ProtCTFFind",
    "object.id": "82",
    "object.label": "ctffind4",
    "object.comment": "\\n",
    "runName": null,
    "runMode": 0,
    "recalculate": false,
    "sqliteFile": null,
    "ctfDownFactor": 1.0,
    "useCftfind4": true,
    "astigmatism": 100.0,
    "findPhaseShift": false,
    "lowRes": 0.05,
    "highRes": 0.35,
    "minDefocus": 0.5,
    "maxDefocus": 4.0,
    "windowSize": 256,
    "hostName": "localhost",
    "numberOfThreads": 4,
    "numberOfMpi": 1,
    "inputMicrographs": "40.__attribute__outputMicrographs"
},
{
    "object.className": "EmanProtBoxing",
    "object.id": "369",
    "object.label": "eman2 - boxer",
    "object.comment": "",
    "runName": null,
    "runMode": 0,
    "inputMicrographs": "40.__attribute__outputMicrographs"
},
{
    "object.className": "ProtUserSubSet",
    "object.id": "380",
    "object.label": "3mics",
    "object.comment": "",
    "runName": null,
    "runMode": 0,
    "other": null,
    "sqliteFile": "Runs/000082_ProtCTFFind/ctfs_selection.sqlite,",
    "outputClassName": "SetOfMicrographs",
    "inputObject": "82.__attribute__outputCTF"
},
{
    "object.className": "XmippProtParticlePicking",
    "object.id": "420",
    "object.label": "xmipp3 - manual picking",
    "object.comment": "",
    "runName": null,
    "runMode": 0,
    "memory": 2.0,
    "inputMicrographs": "40.__attribute__outputMicrographs"
},
{
    "object.className": "XmippProtExtractParticles",
    "object.id": "449",
    "object.label": "extract 3 mics",
    "object.comment": "\\n",
    "runName": null,
    "runMode": 0,
    "micsSource": 0,
    "boxSize": 64,
    "doSort": false,
    "rejectionMethod": 0,
    "maxZscore": 3,
    "percentage": 5,
    "doRemoveDust": true,
    "thresholdDust": 3.5,
    "doInvert": true,
    "doFlip": false,
    "doNormalize": true,
    "normType": 2,
    "backRadius": -1,
    "hostName": "localhost",
    "numberOfThreads": 1,
    "numberOfMpi": 1,
    "ctfRelations": "82.__attribute__outputCTF",
    "inputMicrographs": "369.outputMicrographs"
},
{
    "object.className": "XmippParticlePickingAutomatic",
    "object.id": "517",
    "object.label": "xmipp3 - auto-picking",
    "object.comment": "",
    "runName": null,
    "runMode": 0,
    "micsToPick": 0,
    "memory": 2.0,
    "hostName": "localhost",
    "numberOfThreads": 1,
    "numberOfMpi": 1,
    "xmippParticlePicking": "420"
}
]"""
