import autocomplete_light
from django import forms

class ExampleForm(forms.Form):

    animal =  autocomplete_light.ChoiceField("AnimalsAutocomplete")
