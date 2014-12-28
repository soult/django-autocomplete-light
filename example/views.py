from django.shortcuts import render

from . import forms

def index(request):
    if request.method == "POST":
        form = forms.ExampleForm(request.POST)
    else:
        form = forms.ExampleForm()
    return render(request, "index.html", {"form": form })
