

#from django.forms import ModelForm
from django import forms
from .models import Task

#es un formulario creado por mi para create tasks
#class TaskForm(ModelForm):
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets ={
            'title':forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Write a title"}), #voy a utilizar title en el html class del html
            'description' : forms.Textarea(attrs={'class': 'form-control', 'placeholder':"Write a description"}),
            'important' : forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),

        }
        #widgets es un diccionario para poder utilizarlo en el html