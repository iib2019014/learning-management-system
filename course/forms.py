from django import forms

from course.models import (
    Material,

    MATERIAL_TYPE,
)

class MaterialForm(forms.ModelForm) :

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    material_type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=MATERIAL_TYPE)
    link = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)

    class Meta :
        model = Material
        fields = ('name', 'material_type', 'link', 'file')