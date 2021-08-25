from django.forms import ModelForm

from .models import *


class MainForm(ModelForm):
    class Meta:
        model = Form
        fields = ['title', 'description']


class FormQustions(ModelForm):
    class Meta:
        model = Question
        fields = ['question']


class FormSubmissions(ModelForm):
    class Meta:
        model = Response
        fields = ['answered_by', 'response', 'answered_by_email_id']