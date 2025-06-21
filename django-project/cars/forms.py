from django import forms
from cars.models import Brand, Car

class CarModelForm(forms.ModelForm):
    
    class Meta:
        model = Car
        fields = '__all__'
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 20000:
            self.add_error('price', 'Price must be at least 20.000,00.')
        return price
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1997:
            self.add_error('factory_year', 'Factory year must be at least 1997.')
        return factory_year