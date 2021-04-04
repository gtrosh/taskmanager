from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ("title", "text")
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название задачи',
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание задачи',
            }),
            }
