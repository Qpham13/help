from django.forms import ModelForm
from .models import suggest

class suggestive(ModelForm):
    class Meta:
        model = suggest
        exclude=()

