import autocomplete_light

class AnimalsAutocomplete(autocomplete_light.autocomplete.AutocompleteListBase):

    choices = ["Dog", "Cat", "Lion", "Shark"]

autocomplete_light.register(AnimalsAutocomplete)
