from django import forms
from cars.models import Brand, Car

class CarModelForm(forms.ModelForm):
    
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Value must be at least 20.000,00.')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1997:
            self.add_error('factory_year', 'Factory year must be at least 1997.')
        return factory_year