from django import forms

class CuisineForm(forms.Form):
    cuisine = forms.CharField(label="Cuisine:", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Enter Cuisine'}))
