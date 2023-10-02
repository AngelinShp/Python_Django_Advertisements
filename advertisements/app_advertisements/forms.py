from django import forms

class AdvertisementForms(forms.Form):
    title=forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    description=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
    price=forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
    auction=forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    image=forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}))

