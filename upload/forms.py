from django import forms
from data.models import Workflow, Category, CategoriesAmount

class WorkflowForm(forms.ModelForm):
    name = forms.CharField( max_length=128, help_text="Name: ")
    keywords = forms.CharField(max_length=512, help_text= "Keywords:")
    description = forms.CharField(max_length=512, help_text ="Description: ")
    versionInit = forms.CharField(max_length=512, help_text = "versionInit:")
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), help_text = "Categorias: ")


    class Meta:
        model = Workflow
        exclude=('slug','created','views', 'downloads', 'client_ip')

    def save(self, *args, **kwargs):
        workflow = Workflow()
        workflow.name = self.data['name']
        workflow.keywords = self.data['keywords']
        workflow.versionInit = self.data['versionInit']
        workflow.save()
        categorias = self.cleaned_data['category']
        print '******************'
        print categorias
        for x in categorias:
            print "Dentro del bucle"
            print x
            CategoriesAmount.objects.get_or_create(workflow= workflow, categories= x)

        print CategoriesAmount.objects.filter(workflow = workflow)
        workflow.save()
