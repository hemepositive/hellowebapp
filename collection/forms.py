from django.forms import ModelForm
from .models import Thing

class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ('name', 'description')
