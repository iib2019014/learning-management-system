from django import forms

from course.models import (
    Material,
)

class MaterialForm(forms.ModelForm) :

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # course = forms.ChoiceField()
    material_type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    link = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta :
        model = Material
        fields = '__all__'