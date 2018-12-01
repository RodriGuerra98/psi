from django import forms
from data.models import Workflow, Category, CategoriesAmount

class WorkflowForm(forms.ModelForm):
    name = forms.CharField( max_length=128)
    keywords = forms.CharField(max_length=512)
    description = forms.CharField(max_length=512)
    versionInit = forms.CharField(max_length=512)


    class Meta:
        model = Workflow
        exclude=('slug','created')
