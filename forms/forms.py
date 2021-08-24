from django.forms import ModelForm

from .models import *


class CreatePollForm(ModelForm):
    class Meta:
        model = Form
        fields = ['question', 'option_one', 'option_two']