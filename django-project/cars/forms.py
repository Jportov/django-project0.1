from django import formsg


class CarForm(forms.Form):
    model = forms.CharField(
        max_length=200,
    )
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        label='Brand',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    factory_year = forms.IntegerField(
        label='Factory Year',
        widget=forms.NumberInput(attrs={'placeholder': 'Enter car factory year'})
    )
    model_year = forms.IntegerField(
        label='Model Year',
        widget=forms.NumberInput(attrs={'placeholder': 'Enter car model year'})
    )
    plate = forms.CharField(
        label='Plate',
        max_length=10,
    )
    photo = forms.ImageField(
        label='Image',
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
